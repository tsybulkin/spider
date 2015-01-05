#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from tools import *
import numpy as np

from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import LinearLayer, SigmoidLayer

 
Ls = [-1,0,1]
all_actions = [ (i, j, k, n) for i in Ls for j in Ls for k in Ls for n in Ls ]
		

class nn_agent():
	def __init__(self, lr=0.5, gama=0.7):
		self.Qnet = buildNetwork(20, 16, 1, hiddenclass=SigmoidLayer, bias=True)
		self.Qnet.sortModules()
	
		self.learn_rate = lr
		self.gama = gama

		

	
	def get_policy(self,State):
		if coin(0.2): 
			return self.get_greedy_policy(State)

	
	def get_Q(self,S,Action):
		if S == None: return -1
		inp = get_nn_input(S,Action)
		return self.Qnet.activate(inp)


	def get_greedy_policy(self,State):
		"""returns the best action for the State
		"""
		value_action_list = [ (self.get_Q(State,A), A) for A in all_actions ]
		
		Value, Action = max(value_action_list)
		#print "Max Q value:", Value, Action

		return Action
		

	def learn(self, State,nextState,Action,reward):
		V = self.get_Q(State,Action)
		V1,_ = self.get_value_action(nextState)
		target_value = reward + self.gama * V1
		inp = get_nn_input(State,Action)
		self.DS.appendLinked( inp, target_value )
		


	def get_value_action(self,State):
		values = [ (self.get_Q(State,A),A) for A in all_actions ]
		return max(values)


 
