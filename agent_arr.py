#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from tools import coin
import numpy as np



class Agent():
	def __init__(self, eps=0.15, lr=0.3, gama=0.7):
		self.Q = np.zeros(1<<21)
		self.eps = eps
		self.learn_rate = lr
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
		State_ind = State<<3
		#print "State:",State_ind
		value_action_list = [ (self.Q[State_ind+A_ind], A_ind) for A_ind in range(8) ]
		V,A_ind = max(value_action_list)
		if V != 0:
			return A_ind
		else:
			return None

	
	
	def learn(self, State, nextState, Action, Reward):
		(V1,_) = self.get_value_action(nextState)
		V = self.Q[(State<<3) + Action]
		#print "Value:", V
		
		V_1 = V + self.learn_rate * (Reward + self.gama * V1 - V)
		self.Q[ ( State<<3) + Action ] = V_1
		


	def get_value_action(self,State):
		if State == None:
			return (-1,None)

		State_ind = State<<3
		values = [ (self.Q[(State_ind+A_ind)], A_ind) for A_ind in range(8) ]
		V,A = max(values)
		if V == 0:
			return (0,None)
		else:
			return V,A


def index_to_action(Action):
	if Action & 0b100:
		if Action & 0b010:
			if Action & 0b001:
				return (1,0,0,0)
			else:
				return (-1,0,0,0)
		else:
			if Action & 0b001:
				return (0,1,0,0)
			else:
				return (0,-1,0,0)
	else:
		if Action & 0b010:
			if Action & 0b001:
				return (0,0,1,0)
			else:
				return (0,0,-1,0)
		else:
			if Action & 0b001:
				return (0,0,0,1)
			else:
				return (0,0,0,-1)


