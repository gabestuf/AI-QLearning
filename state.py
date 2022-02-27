import numpy as np
import random as random
from board import Board
class State:
	def __init__(self, coord, board):
		self.isEnd = False
		self.coord = coord
		self.val = board[coord[0], coord[1]]

	def giveReward(self):
		if self.val == 1:
			self.isEnd = True
			return 1
		elif self.val == -1:
			self.isEnd = True
			return -1
		else:
			return -0.4

	def _chooseAction(self, action):	#Choose action with some probability
		if action == "up":
			return np.random.choice(["up","left","right"], p=[0.8,0.1,0.1])
		if action == "down":
			return np.random.choice(["down", "left", "right"], p = [0.8,0.1,0.1])
		if action == "left":
			return np.random.choice(["left", "up", "down"], p = [0.8,0.1,0.1])
		if action == "right":
			return np.random.choice(["right", "up", "down"], p = [0.8,0.1,0.1])

	def nextState(self,action): #Given an action, return the next state
		action = self._chooseAction(action)	#Choose random action
		nextCoord = self.nextState(action)	
		#Check legal state
		if(nextCoord[0] >= 0) and (nextCoord[0] <= 50):
			if(nextCoord[1] >= 0) and (nextCoord[1] <= 50):
				return nextCoord
		return self.state

	def isEnd(self):
		if(self.val == 1 or self.val== -1):
			self.isEnd = True
		return True
