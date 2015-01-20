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

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet

		

class nn_agent():
	def __init__(self, actions=8, lr=0.5, gama=0.9, eps = 0.15):
		self.Qnets = {}
		for a in actions:
			self.Qnets[a] = buildNetwork(20, 16, 1, hiddenclass=SigmoidLayer, bias=True) 
			self.Qnets[a].sortModules()
	
		self.learn_rate = lr
		self.gama = gama
		self.eps = eps

		self.DS = SupervisedDataSet( 20, 1 )
			

	def get_actions(self):
		return range(8)

	
	def get_policy(self,State):
		if coin(self.eps): 
			return self.get_greedy_policy(State)

	
	def get_Q(self,S,Action):
		if S == None: return -1
		inp = get_nn_input(S,Action)
		return self.Qnets[Action].activate(inp)


	def get_greedy_policy(self,State):
		"""returns the best action for the State
		"""
		value_action_list = [ (self.get_Q(State,A), A) for A in self.get_actions() ]
		
		Value, Action = max(value_action_list)
		#print "Max Q value:", Value, Action

		return Action
		

	def learn(self, State,nextState,Action,reward):
		self.DS = SupervisedDataSet( 20, 1 )
		
		V = self.get_Q(State,Action)		
		for a in all_actions:
			inp = get_nn_input(State,a)
				
			if a == Action:	
				V1,_ = self.get_value_action(nextState)
				target_value = reward + self.gama * V1
				self.DS.appendLinked( inp, target_value )
			else:
				self.DS.appendLinked( inp, V )

		trainer = BackpropTrainer( self.Qnet, dataset=self.DS, momentum=0.5, verbose=False, weightdecay=0.01)
		trainer.train()



	def get_value_action(self,State):
		values = [ (self.get_Q(State,A),A) for A in all_actions ]
		return max(values)



	def index_to_action(self,Action):
		return Action
 
