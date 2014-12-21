#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 



class Leg():
	def __init__(self,index, attach_angle, raised=False, phi=0, d=3, L=6):
		self.index = index
		self.aa = attach_angle
		self.phi = phi
		self.d = phi
		self.L = L
		self.raised = raised

