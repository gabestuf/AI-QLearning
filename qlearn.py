
import sys
import argparse
import random

from board_generator import generateBoard
from board import *


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('usage python astar.py [boardPath] [runTime] [probability] [reward]')
        exit()

    

    # TESTING
    # args = ["qlearn.py","boards/board1.txt", 1.3, 0.9,-0.05]

    print('Command Arguments:', sys.argv)

    # generate a board
    # generateBoard()

    # board class
    b = Board(sys.argv[1])


