
import sys
import argparse
import random
import sys
from agent import *
from board import *


def visualize(actions):
    
    upVal = actions['up']
    downVal = actions['down']
    leftVal = actions['left']
    rightVal = actions['right']
    list = [upVal, downVal, leftVal, rightVal]

    bestVal = 0
    bestAction = ''

    if max(list) == list[0]:
        bestAction = 'up'
        bestVal = list[0]
    elif max(list) == list[1]:
        bestAction = 'down'
        bestVal = list[1]
    elif max(list) == list[2]:
        bestAction = 'left'
        bestVal = list[2]
    elif max(list) == list[3]:
        bestAction = 'right'
        bestVal = list[3]

    return bestAction, bestVal


if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print('usage python qlearn.py [boardPath] [runTime] [probability] [reward]')
        exit()
    
    args = sys.argv
    
    # TESTING
    # args = ["qlearn.py","boards/board10x10.txt", 1, 0.9,-0.05]

    b = Board(args[1])
    time = float(args[2])
    prob = float(args[3])
    reward = float(args[4])
    #print('Command Arguments:', sys.argv)
    a = Agent(b,prob)
    a.qLearn(time,reward)

    for val in a.qVals:
        print("Location: ", val, " | Best Action/Score: ", visualize(a.qVals[val]))

    



