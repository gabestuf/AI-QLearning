import numpy as np
import random as random
from state import State


class Agent:
	def __init__(self, board):
		"""
		Initialize the agent.
		:param board: Board object.
		"""
		self.states = [] #position and action taken at that position
		self.moves = ["up", "down", "left", "right"]
		self.State = State()
		self.isEnd = self.State.isEnd
		self.lr = 0.2
		self.expRate = 0.3
		self.gamma = 0.9

	def chooseAction(self):
		# Choose action with most expected value
		maxNextReward = 0
		action = ""

		if np.random.uniform(0,1 <= self.expRate):
			action = np.random.choice(self.actions)
		return action

	def play(self, rounds=10):
		i = 0
		while i < rounds:
			# to the end of game back propagate reward
			if self.State.isEnd:
				# back propagate
				reward = self.State.giveReward()
				for a in self.actions:
					self.Q_values[self.State.state][a] = reward
				print("Game End Reward", reward)
				for s in reversed(self.states):
					current_q_value = self.Q_values[s[0]][s[1]]
					reward = current_q_value + self.lr * (self.decay_gamma * reward - current_q_value)
					self.Q_values[s[0]][s[1]] = round(reward, 3)
				self.reset()
				i += 1
			else:
				action = self.chooseAction()
				# append trace
				self.states.append([(self.State.state), action])
				print("current position {} action {}".format(self.State.state, action))
				# by taking the action, it reaches the next state
				self.State = self.takeAction(action)
				# mark is end
				self.State.isEndFunc()
				print("nxt state", self.State.state)
				print("---------------------")
				self.isEnd = self.State.isEnd