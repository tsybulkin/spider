#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 
import sys

from random import seed
import agent, agent_arr
from nn_agent import nn_agent

import spider, spider_arr

from tools import *

import numpy as np
import matplotlib.pyplot as plt

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet



def get_action(State,Action,robot,agent):
	robot_copy = robot.copy()
		
	reward, nextState = robot_copy.take_action(Action)
	#print "Reward, State:",reward,nextState
	agent.learn(State,nextState,Action,reward)
	if nextState == None:
		pass
	else:
		robot = robot_copy.copy()
	return robot



def get_random_action(State, robot, agent):
	Actions = robot.get_actions()
	while len(Actions) > 0:
		Action = choose_randomly(Actions)
		return get_action(State,Action,robot,agent)
					



def run(episodes, mode):
	seed()
	
	if mode == 'neural':
		agent = nn_agent()
	elif mode == 'salsa_dict':
		agent = agent.Agent()
		data = read_data("data/spider.dat")
		if data != None:
			agent.Q = data
	elif mode == 'salsa_arr':
		agent = agent_arr.Agent()
		data = read_data("data/spider_arr.dat")
		if data != None:
			agent.Q = data
	else:
		raise
	
	
	for i in range(episodes):
		if i%10000 == 0: print "%i episodes passed." % i
		
		if mode == 'salsa_arr':
			robot = spider_arr.Spider()
		else:
			robot = spider.Spider()

		agent.DS = SupervisedDataSet( 20, 1 )
		
		run_episode(robot,agent,False)
		if mode == 'neural':
			trainer = BackpropTrainer( agent.Qnet, dataset=agent.DS, momentum=0.5, verbose=False, weightdecay=0.01)
			trainer.train()

		
	
	## demo what has been leartn
	_ = raw_input("press key to watch the demo")
	run_episode(robot,agent,True,episode_len=100)


	if mode == 'neural':
		pass
	elif mode == 'salsa_dict':
		agent.clean_q()
		print "State-action remained:", len(agent.Q)
		write_data(agent.Q,"data/spider.dat")
	elif mode == 'salsa_arr':
		write_data(agent.Q,"data/spider_arr.dat")
	

	



def run_episode(robot, agent, draw,episode_len=100):
	
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
		#print "State:",State
		policy = agent.get_policy(State)
		#print "Policy:", policy
		if policy == None:
			robot = get_random_action(State, robot, agent)	
		else:
			robot = get_action(State,policy,robot, agent)
			
	if robot.xy0[0]>12:
		print "xy: %s" % robot.xy0
	return 1		





if __name__ == '__main__':
	Args = sys.argv[:]
	if len(Args) != 3:
		print "Wrong syntax\nUSAGE: python run.py <nbr_training_episodes> agent"
		print "Available agents: \n\tneural\n\tsalsa"
	else:
		run(int(Args[1]),Args[2])

