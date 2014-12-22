#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 

from tools import coin



class Agent():
	def __init__(self, eps=0.05, lr=0.5, gama=0.9):
		self.Q = {}
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
		value_action_list = [ (self.Q[(S,A)], A) for (S,A) in self.Q if S == State]
		
		if len(value_action_list) != 0:
			Value, Action = max(value_action_list)
			return Action
		else:
			return None

	
	
	def learn(self, State, nextState, Action, Reward):
		(V1,_) = self.get_value_action(nextState)
		V = self.Q.get((State,Action),0)
		
		V_1 = V + self.learn_rate * (Reward + self.gama * V1 - V)
		if V_1 > 0.01:
			self.Q[ ( State, Action) ] = V_1
		elif ( State, Action) in self.Q:
			del self.Q[( State, Action)]



	def get_value_action(self,State):
		values = [ (self.Q[(S,A)],A) for (S,A) in self.Q if S == State ]
		if len(values) == 0:
			return (0,None)
		else:
			return max(values)


	def clean_q(self):
		"""removes worst records in Q dictionary
		"""
		States = set([ S for (S,_) in self.Q])
		print "There is %i unique states" % len(States)

		to_del = []
		for key in self.Q:
			if self.Q[key] < 0.01: to_del.append(key)
		print "%i records will be deleted" % len(to_del)

		for key in to_del:
			del self.Q[key]
		"""
		for State in States:
			actions = [ (self.Q[(S,A)], A) for (S,A) in self.Q if S == State]
			if len(actions) < 10: continue
			
			actions.sort()
			worst = actions[:len(actions)/2]
			
			for (V,A) in worst:
				del self.Q[(State,A)] 
		"""







