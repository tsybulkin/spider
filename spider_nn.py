#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from leg import Leg

import nn_agent

from math import sin,cos,radians,degrees,pi,asin,atan,sqrt
from time import sleep
import numpy as np
from tools import *


dR_BODY = 0.3
dR_LEG = 0.9


class Spider():
	def __init__(self,theta=0):
		# spider dimensions
		self.R = 5
		self.h = 1
		
		self.xy0 = np.array([0,0])
		self.CM = np.array([0,0])
		self.theta = theta

		delta = 0.1
		self.legs = [ Leg( index=i, 
							attach_angle=theta-delta/2+(pi/2+delta/3)*i, 
							raised = i==0, 
							d=5+delta*i ) for i in range(4) ]


	def copy(self):
		copy = Spider()
		copy.xy0 = self.xy0
		copy.theta = self.theta
		copy.legs = []
		for leg in self.legs:
			l = Leg(leg.index,leg.aa,leg.raised,leg.phi,leg.d)
			copy.legs.append(l)

		return copy

	
	def get_raised_leg(self):
		for leg in self.legs:
			if leg.raised: return leg


	def get_state(self):
		"""returns 12-dimensional state of the spider. 
		Xo,Yo and 'theta' are not included to the state
		"""
		return tuple([ ( nn_angle(leg.phi), nn_dist(leg.d), leg.raised )  
			for leg in self.legs])



	def get_move(self,Action):
		return()


	def take_action(self, Action):
		"""take action and gets to the next State
		returns reward and nextState
		"""
		xy_old = sum([ leg.get_xy((self.xy0,self.R,self.theta)) for leg in self.legs ])
		
		(i,j, k,n) = self.get_move(Action)
		#(i,j, k,n) = nn_agent.index_to_action(Action)
		#print "\nAction:",Action
		
		raised_leg = self.get_raised_leg()
		d_phi = dR_LEG * n / raised_leg.d
		raised_leg.d += dR_LEG * k
		if raised_leg.legal(d_phi,raised_leg.d):
			raised_leg.phi += d_phi
		else:
			return (-1,None)	

		dxy = np.array([dR_BODY*( i*cos(self.theta) - j*sin(self.theta)), 
						dR_BODY*( i*sin(self.theta) + j*cos(self.theta)) ])
		#print "dxy:",dxy
		for leg in self.legs:
			if not leg.update(self.xy0, dxy, self.R, self.theta):
				return (-1,None)
		
		self.xy0 = self.xy0[:]+dxy
		#print "reward:",reward
		xy_new = sum([ leg.get_xy((self.xy0,self.R,self.theta)) for leg in self.legs ])
		dxy1 = xy_new - xy_old
		## check if raised leg changed
		self.check_raised_leg()
		reward = dxy1[0] - abs(dxy1[1])/3 - 0.01	
		

		return (reward, self.get_state())

	
	def draw(self,plt):
		ps = plt.gca().patches
		while len(ps) >1: ps.pop() 
		
		circle = plt.Circle(tuple(self.xy0), radius=self.R, fc='r')
		plt.gca().add_patch(circle)
		
		for leg in self.legs:
			if leg.raised: color = 'r'
			else: color = 'b'

			foot = plt.Circle(leg.get_xy((self.xy0,self.R,self.theta)), radius=self.R/5, fc=color)	
			plt.gca().add_patch(foot)
		plt.draw()
		sleep(0.4)


	def check_raised_leg(self):
		leg_raised = self.get_raised_leg()
		raised = leg_raised.index
		leg1 = self.legs[(raised+3)%4]
		leg2 = self.legs[(raised+1)%4]

		body = self.xy0,self.R,self.theta
		f1 = leg1.get_xy(body)
		f2 = leg2.get_xy(body)
		self.CM = (f1+f2)/2
		if np.cross( f2-f1, self.xy0-f1) > 0: return
		
		leg0 = self.legs[(raised+2)%4]
		fo = leg0.get_xy(body)
		fr = leg_raised.get_xy(body)	
		if np.cross(fr-fo,self.xy0-fo) > 0:
			leg1.raised = True
		else:
			leg2.raised = True

		leg_raised.raised = False
		




