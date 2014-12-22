#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from tools import coin
import numpy as np

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
 
Ls = [-1,0,1]
all_actions = [ (i, j, k, n) for i in Ls for j in Ls for k in Ls for n in Ls ]


class nn_agent():
	def __init__(self, lr=0.5, gama=0.9):
		self.Qnet = buildNetwork(20, 7, 1, hiddenclass=SigmoidLayer, bias=True)
		self.Qnet.sortModules()
	
		self.learn_rate = lr
		self.gama = gama

	
	def get_policy(self,State):
		return self.get_greedy_policy(State)

	def get_Q(self,S,Action):
		AA = [ (int(A==1),int(A==-1)) for A in Action ]
		return self.Q.activate(np.array([S[0][0],S[0][1],S[0][2],
										S[1][0],S[1][1],S[1][2],
										S[2][0],S[2][1],S[2][2],
										S[3][0],S[3][1],S[3][2],
										AA[0][0],AA[0][1],
										AA[1][0],AA[1][1],
										AA[2][0],AA[2][1],
										AA[3][0],AA[3][1] ]) )


	def get_greedy_policy(self,State):
		"""returns the best action for the State
		"""
		value_action_list = [ (self.get_Q(State,A), A) for A in all_actions ]
		
		Value, Action = max(value_action_list)
		print "Max Q value:", Value

		return Action
		

 
