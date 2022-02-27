
import argparse
import random
from board import Board
from agent import Agent

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

  
    b = Board(args.file)
    time = args.seconds
    prob = args.probability
    reward = args.reward

    a = Agent(b,prob)
    a.qLearn(time,reward)
    


