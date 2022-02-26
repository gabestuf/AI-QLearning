import numpy as np
import random as random


class State:
    def __init__(self, board):

        self.isEnd = False
        self.state = (random.randint(0, 49), random.randint(0, 49))

    def _chooseAction(self, action):
        if action == "up":
            return np.random.choice

    def giveReward(self):
        if self.state != 1:
            return 1
        elif self.state == -1:
            return -1
        else:
            return -0.4

    def isEnd(self):
        if (self.state == 1) or (self.state == -1):
            self.isEnd = True

    def _chooseMove(self, action):
        if action == "up":
            return np.random.choice(["up", "left", "right"], p=[0.8, 0.1, 0.1])
        if action == "down":
            return np.random.choice(["down", "left", "right"], p=[0.8, 0.1, 0.1])
        if action == "left":
            return np.random.choice(["left", "up", "down"], p=[0.8, 0.1, 0.1])
        if action == "right":
            return np.random.choice(["right", "up", "down"], p=[0.8, 0.1, 0.1])

    def nextPosition(self, action):
        action = self._chooseMove(action)
        next_state = self.nextPosition(action)
        # Check legal state
        if (next_state[0] >= 0) and (next_state[0] <= 50):
            if (next_state[1] >= 0) and (next_state[1] <= 50):
                if next_state != (1, 1):
                    return next_state
        return self.state
