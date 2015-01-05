#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from random import random
import os
import pickle
import numpy as np

from leg import phi_max, d_max


angle_discrete = phi_max / 2.0  # discrete angle changes from 0 to 3
dist_discrete = d_max / 4.0 # discrete d changes from 0 to 3


def coin(p): return p > random()


def choose_randomly(Ls):
	"""chooses random element fro the list. 
	returns chosen element and removes it from the list
	""" 
	N = len(Ls)
	return Ls.pop(int(N*random()))
	

def d_angle(angle): return int( (angle+phi_max)/angle_discrete )


def d_dist(distance): return int( (d_max-distance)/dist_discrete )


def read_data(my_file):
	if not os.path.isfile(my_file):
		return None

	with open(my_file, 'rb') as handle:
  		data = pickle.loads(handle.read())
  	handle.close()

  	return data


def write_data(data, my_file):
	with open(my_file, 'wb') as handle:
		pickle.dump(data, handle)
	handle.close()


def get_nn_input(S,Action):
	AA = [ (int(A==1),int(A==-1)) for A in Action ]
	return np.array([S[0][0],S[0][1],S[0][2],
					S[1][0],S[1][1],S[1][2],
					S[2][0],S[2][1],S[2][2],
					S[3][0],S[3][1],S[3][2],
					AA[0][0],AA[0][1],
					AA[1][0],AA[1][1],
					AA[2][0],AA[2][1],
					AA[3][0],AA[3][1] ]) 
