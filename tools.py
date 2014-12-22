#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from random import random
import os
import pickle


angle_discrete = 0.3
dist_discrete = 2


def coin(p): return p < random()


def choose_randomly(Ls):
	"""chooses random element fro the list. 
	returns chosen element and removes it from the list
	""" 
	N = len(Ls)
	return Ls.pop(int(N*random()))
	

def d_angle(angle): return int(round(angle/angle_discrete))


def d_dist(distance): return int(round(distance/dist_discrete))


def read_data(my_file):
	if not os.path.isfile(my_file):
		return {}

	with open(my_file, 'rb') as handle:
  		data = pickle.loads(handle.read())
  	handle.close()

  	return data


def write_data(data, my_file):
	with open(my_file, 'wb') as handle:
		pickle.dump(data, handle)
	handle.close()


