#!/usr/bin/python
#
# spider robot
#  
#
####################################################### 
from random import seed
from agent import Agent
from spider import Spider

from tools import *



episode_len = 40


def get_action(State,Action,robot,agent):
	robot_copy = robot.copy()
		
	reward, nextState = robot_copy.take_action(State,Action)
	agent.learn(State,nextState,policy,reward)
	return robot_copy



def get_random_action(State, robot, agent):
	Actions = robot.get_actions()
	while len(Actions) > 0:
		Action = choose_randomly(Actions)
		robot1 = get_action(State,Action,robot,agent)
		if robot1 != None:
			return robot1

	return None
				



def run(episodes):

	seed()
	agent = Agent()
	
	for i in range(episodes):
		robot = Spider()
		run_episode(robot,agent)


	## demo what has been leartn
	



def run_episode(robot, agent):

	for N in range(episode_len):	
		
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
	if len(Args) != 2:
		print "Wrong syntax\nUSAGE: python run.py <nbr_training_episodes> "
	else:
		run(int(Args[1]))

