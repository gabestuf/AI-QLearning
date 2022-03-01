from tracemalloc import start
import numpy as np
import time as time
from state import State

class Agent:
	def __init__(self, board, prob):
		self.states = [] #position and action taken at that position
		self.actions = ["up","down","left","right"]						
		self.qVals = {}
		self.isEnd = False
		self.prob = prob
		self.board = board

		#Agent starts at a random state
		randCoord = board.getRandomCoord()
		self.state = State(randCoord, board)
		while(self.state.isEnd):
			self.state = State(board.getRandomCoord(board),board)

		#Initializing Q table
		print(len(board.map) - 1)
		print(len(board.map[0]) - 1)
		for i in range(len(board.map)):
			for j in range(len(board.map[0])):
				self.qVals[(i,j)] = {}
				for a in self.actions:
					self.qVals[(i,j)][a] = 0

	def chooseAction(self):
		maxNextReward = 0

		if np.random.uniform(0,1) <= 0.3: #Exploration
			action = np.random.choice(self.actions)
		else:
			for a in self.actions:	#Greedy
				currentPos = self.state.coord
				nextReward = self.qVals[currentPos][a]
				if nextReward >= maxNextReward:
					action = a
					maxNextReward = nextReward
				if nextReward == 0:
					action = np.random.choice(self.actions)
				if nextReward < maxNextReward:
					action = np.random.choice(self.actions)
		return action

	def takeAction(self, action):
		coord = self.state.nextState(action, self.prob)
		return State(coord, self.board)

	def reset(self):
		self.states = []
		randCoord = self.board.getRandomCoord()
		self.state = State(randCoord, self.board)
		while(self.state.isEnd):
			self.state = State(self.board.getRandomCoord(self.board),self.board)

	def qLearn(self, seconds, reward):
		elapsedTime = 0
		startTime = time.time()
		while elapsedTime < seconds:
			currentTime = time.time()
			if self.state.isEnd:
				newReward = self.state.giveReward(reward)
				for a in self.actions:
					self.qVals[self.state.coord][a] = newReward
				print("Game end Reward - ", newReward)
				for s in reversed(self.states):
					current_q_value = self.qVals[s[0]][s[1]]
					newReward = current_q_value + 0.2 * (0.9 * newReward - current_q_value)
					self.qVals[s[0]][s[1]] = round(newReward, 3)
				self.reset()
				elapsedTime = currentTime - startTime
			else:
				action = self.chooseAction()
				self.states.append([(self.state.coord), action])
				print("current position {} action {}".format(self.state.coord, action))
				self.state = self.takeAction(action)
				self.state.isEndF()
				print("Next state - ", self.state.coord)
				print("---------------------")
				self.isEnd = self.state.isEnd
				elapsedTime = currentTime - startTime
			