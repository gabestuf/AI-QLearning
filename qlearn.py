
import argparse

from board import *
from board_generator import generateBoard


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file',
        help="--file : The name of the file to read in representing the map",
        type=str
    )

    parser.add_argument(
        'seconds',
        help="--seconds : How long to learn (in seconds)",
        type=float
    )

    parser.add_argument(
        'probability',
        help="-- probability : The probability of moving in the desired direction upon taking an action",
        type=float
    )

    parser.add_argument(
        'reward',
        help="--reward : The constant reward for each action. ",
        type=float
    )

    args = parser.parse_args()

    # TESTING

    print('Command Arguments:', args)

    # generate a board
    rows = 5
    cols = 5
    percentOfNonZeroNumbers = 0.1
    lowest = -1
    highest = 1
    generateBoard(1, rows, cols, percentOfNonZeroNumbers, lowest, highest)

    # board class
    b = Board(args.file)
