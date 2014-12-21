#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from leg import Leg

from math import sin,cos,radians,degrees,pi,asin,atan,sqrt
from time import sleep
import numpy as np
from tools import *


alpha_max = pi/2
beta_max = pi
phi_max = pi/5

r_body = 0.2
r_leg = 0.5


class Spider():
	def __init__(self,theta=0):
		# spider dimensions
		self.R = 5
		self.h = 1
		
		self.x0 = 0
		self.y0 = 0
		self.theta = theta

		self.legs = [ Leg( index=i, attach_angle=theta+pi/2*i, raised=i==0 ) for i in range(4) ]


	def copy(self):
		copy = Spider()
		copy.x0 = self.x0
		copy.y0 = self.y0
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
		return tuple([ ( d_angle(leg.phi), d_dist(leg.d), leg.raised )  
			for leg in self.legs])



	def get_actions(self):
		"""returns a list of all actions
		action = (rn,rt,rn,rt) for body and for free leg
		"""
		Ls = [-1,0,1]
		return [ (i, j, k, n) for i in Ls for j in Ls for k in Ls for n in Ls ]



	def take_action(self, Action):
		"""take action and gets to the next State
		returns reward and nextState
		"""
		x_old = self.x0
		y_old = self.y0

		(i,j, k,n) = Action
		
		raised_leg = self.get_raised_leg()
		raised_leg.phi += r_leg*n/raised_leg.d
		raised_leg.d += r_leg*k
		
		
		return (0, self.get_state())

	
	def draw(self,plt):
		ps = plt.gca().patches
		while len(ps) >1: ps.pop() 
		
		circle = plt.Circle((self.x0,self.y0), radius=self.R, fc='r')
		plt.gca().add_patch(circle)
		
		for leg in self.legs:
			if leg.raised: color = 'r'
			else: color = 'b'

			foot = plt.Circle(leg.get_xy(self.x0,self.y0,self.R,self.theta), radius=self.R/5, fc=color)	
			plt.gca().add_patch(foot)
		plt.draw()
		sleep(0.5)




