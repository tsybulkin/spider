#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from math import sin, cos


class Leg():
	def __init__(self,index, attach_angle, raised=False, phi=0, d=5, L=6):
		self.index = index
		self.aa = attach_angle
		self.phi = phi
		self.d = d
		self.L = L
		self.raised = raised


	def get_xy(self,x0,y0,R,theta):
		return (x0 + R*cos(theta+self.aa) + self.d*cos(theta+self.aa+self.phi),
				y0 + R*sin(theta+self.aa) + self.d*sin(theta+self.aa+self.phi))