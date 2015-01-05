#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from math import sin, cos, asin, pi
import numpy as np


d_min = 1.0
d_max = 9.0
phi_max = pi/4


class Leg():
	def __init__(self,index, attach_angle, raised=False, phi=0, d=5, L=6):
		self.index = index
		self.aa = attach_angle
		self.phi = phi
		self.d = d
		self.L = L
		self.raised = raised


	def get_xy(self,(xy0,R,theta)):
		x0,y0 = xy0
		return np.array([x0 + R*cos(theta+self.aa) + self.d*cos(theta+self.aa+self.phi),
						y0 + R*sin(theta+self.aa) + self.d*sin(theta+self.aa+self.phi) ])

	def legal(self, d_phi, d): 
		return d > d_min and d < d_max and abs(self.phi+d_phi) < phi_max


	def update(self,xy0,dxy,R,theta):
		if self.raised: return True

		joint = xy0 + np.array([R*cos(theta+self.aa),
								R*sin(theta+self.aa) ]) 
		joint1 = joint + dxy
		foot = self.get_xy((xy0,R,theta))

		v = foot - joint
		v1= foot - joint1

		d1 = np.linalg.norm(v1)
		d_phi = asin( np.cross(v,v1) / (self.d*d1) )
		
		if self.legal(d_phi,d1):
			self.phi += d_phi
			self.d = d1
			return True
		else:
			return False


		

