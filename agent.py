#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

#from tools import d, coin
from math import pi



class Agent():
	def __init__(self, eps=0.1, lr=0.5, gama= 0.9):
		self.Q = {}
		self.eps = eps
		self.lean_rate = lr
		self.gama = gama

	
	def get_policy(self,State):
		return self.get_eps_policy(State)


	def get_eps_policy(self,State):
		if coin(self.eps):
			return None
		else:
			return self.get_greedy_policy(State)


	

	def get_greedy_policy(self,State):
		"""returns the best action for the State
		"""
		value_action_list = [ (self.Q[(S,A)], A) for (S,A) in self.Q if S == State]
		
		if len(value_action_list) != 0:
			value_action_list.sort()
			Value, Action = value_action_list.pop()
			print "Value:%.2g, actions: %i" %(Value,len(value_action_list)+1)
			#print value_action_list
			return Action
		else:
			return None

	def learn(self, nextState, State, Action, Reward):
		V1 = get_value(nextState)
		V = get_value(State)
		
		V_1 = V + self.lr * (Reward + self.gama * V1 - V)
		self.Q[ ( State, Action) ] = V_1



	def get_value(self,State):
		values = [ self.Q[(S,A)] for (S,A) in self.Q if S == State]
		if len(values) == 0:
			return 0
		else:
			return max(values)



def get_reward(State, nextState, Action):
	"""returns the next state and reward
	"""
	return 0





