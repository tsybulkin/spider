#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from random import random



def coin(p): return p < random()


def choose_randomly(Ls):
	"""chooses random element fro the list. 
	returns chosen element and removes it from the list
	""" 
	N = len(Ls)
	return Ls.pop(int(N*random()))
	