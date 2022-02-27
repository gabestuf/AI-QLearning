import numpy as np
import random as random
from state import State

class Agent:
	def __init__(self, board):
		self.states = [] #position and action taken at that position
		self.moves = ["up","down","left","right"]						
		self.qVal = {}
		self.isEnd = False

		#Agent starts at a radnom state
		randCoord = board.getRandomCoord()
		self.state = State(randCoord, board)
		while(self.state.isEnd):
			self.state = State(board.getRandomCoord(board),board)

		#Initializing Q table
		for i in range(len(board.map)):
			for j in range(len(board.map[0])):
				self.qVals[(i,j)] = {}
				for a in self.actions:
					self.qVals[(i,j)][a] = 0

	def chooseAction(self):
		#Greedy choose action
		maxNextReward = 0
		action = ""

		for a in self.moves:
			currentPos = self.state.coord
			nextReward = self.qVals[currentPos][a]
			if nextReward >= maxNextReward:
				action = a
				maxNextReward = nextReward
		return action

	def takeAction(self, action):
		coord = self.State.nextPosition(action)
		return State(state=coord)

	def qLearn(self, time):
		pass
