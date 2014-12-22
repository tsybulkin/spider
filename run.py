#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 
import sys

from random import seed
from agent import Agent
#from nn_agent import nn_agent

from spider import Spider

from tools import *

import numpy as np
import matplotlib.pyplot as plt





def get_action(State,Action,robot,agent):
	robot_copy = robot.copy()
		
	reward, nextState = robot_copy.take_action(Action)
	agent.learn(State,nextState,Action,reward)
	return robot_copy



def get_random_action(State, robot, agent):
	Actions = robot.get_actions()
	while len(Actions) > 0:
		Action = choose_randomly(Actions)
		robot1 = get_action(State,Action,robot,agent)
		if robot1 != None:
			return robot1

	return None
				



def run(episodes, mode):
	seed()
	
	if mode == 'neural':
		agent = nn_agent()
	else:
		agent = Agent()
		agent.Q = read_data("data/spider.dat")	
	
	
	for i in range(episodes):
		if i%500 == 0: print "%i episodes passed. %i state-actions processed" % (i,len(agent.Q))
		robot = Spider()
		run_episode(robot,agent,False)
		
	print "State-action processed:", len(agent.Q)

	## demo what has been leartn
	run_episode(robot,agent,True,episode_len=50)


	if mode == 'neural':
		pass
	else:
		agent.clean_q()
		print "State-action remained:", len(agent.Q)
		write_data(agent.Q,"data/spider.dat")
	

	



def run_episode(robot, agent, draw,episode_len=20):
	
	if draw:
		plt.axes()
		rectangle = plt.Rectangle((-25, -25), 60, 60, fc='w')
		plt.gca().add_patch(rectangle)
		plt.axis('scaled')
		plt.ion()
		plt.show()
		
	for _ in range(episode_len):	
		if draw: robot.draw(plt)

		State = robot.get_state()
		policy = agent.get_policy(State)
		if policy == None:
			robot = get_random_action(State, robot, agent)
			if robot == None: return -1
				
		else:
			robot1 = get_action(State,policy,robot,agent)
			if robot1 == None:
				robot = get_random_action(State, robot, agent)
				if robot == None: return -1

	
	return 1		





if __name__ == '__main__':
	Args = sys.argv[:]
	if len(Args) != 3:
		print "Wrong syntax\nUSAGE: python run.py <nbr_training_episodes> agent"
		print "Available agents: \n\tneural\n\tsalsa"
	else:
		run(int(Args[1]),Args[2])

