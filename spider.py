#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from leg import Leg

from math import sin,cos,radians,degrees,pi,asin,atan,sqrt
import numpy as np
#from tools import *
from time import sleep


alpha_max = pi/2
beta_max = pi
phi_max = pi/5


class Spider():
	def __init__(self,theta=0):
		# spider dimensions
		self.R = 5
		self.h = 1
		
		self.x0 = 0
		self.y0 = 0
		self.theta = theta

		self.legs = [ Leg( index=i, attach_angle=theta+pi/2*i, raised=i==0 ) for i in range(4) ]




