import node
import math


class Agent:
	def __init__(self, board):
		"""
		Initialize the agent.
		:param start: Start position on the board.
		:param goal: Goal position on the board.
		:param board: Board object.
		"""
		self.states = [] #position and action taken at that position
		self.moves = ["up","down","left","right"]
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

