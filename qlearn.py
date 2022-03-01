
import sys
import argparse
import random
import sys
from agent import *
from board import *


if __name__ == '__main__':
    """
    if len(sys.argv) != 5:
        print('usage python qlearn.py [boardPath] [runTime] [probability] [reward]')
        exit()
    """
    
    # TESTING
    args = ["qlearn.py","boards/board10x10.txt", 10, 0.9,-10]

    b = Board(args[1])
    time = args[2]
    prob = args[3]
    reward = args[4]
    #print('Command Arguments:', sys.argv)
    a = Agent(b,prob)
    a.qLearn(time,reward)
    print(a.qVals)



