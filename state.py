import numpy as np
import random as random
from board import Board
class State:
	def __init__(self, coord, board):
		self.isEnd = False
		self.coord = coord
		print(type(coord[0]))
		self.val = board.map[coord[0]][coord[1]]

	def giveReward(self,reward):
		if self.val == 1:
			self.isEnd = True
			return 1
		elif self.val == -1:
			self.isEnd = True
			return -1
		else:
			return reward

	def _chooseAction(self, action, prob):	#Choose action with some probability
		likely = prob
		unlikely = (1-prob)/2
		if action == "up":
			return np.random.choice(["up","left","right"], p=[likely,unlikely,unlikely])
		if action == "down":
			return np.random.choice(["down", "left", "right"], p = [likely,unlikely,unlikely])
		if action == "left":
			return np.random.choice(["left", "up", "down"], p = [likely,unlikely,unlikely])
		if action == "right":
			return np.random.choice(["right", "up", "down"], p = [likely,unlikely,unlikely])

	def nextState(self,action, prob): #Given an action, return the next state
		action = self._chooseAction(action, prob)	#Choose random action
		nextCoord = self.nextState(action, prob)	
		#Check legal state
		if(nextCoord[0] >= 0) and (nextCoord[0] <= 50):
			if(nextCoord[1] >= 0) and (nextCoord[1] <= 50):
				return nextCoord
		return self.state

	def isEnd(self):
		if(self.val == 1 or self.val== -1):
			self.isEnd = True
		return True
