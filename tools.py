#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from random import random

angle_discrete = 0.1
dist_discrete = 1


def coin(p): return p < random()


def choose_randomly(Ls):
	"""chooses random element fro the list. 
	returns chosen element and removes it from the list
	""" 
	N = len(Ls)
	return Ls.pop(int(N*random()))
	

def d_angle(angle): return int(round(angle/angle_discrete))


def d_dist(distance): return int(round(distance/dist_discrete))


