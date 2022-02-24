
import argparse





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
    # args = argparse.Namespace('board1.txt', 1.3, 0.9, -0.05)

    print('Command Arguments:', args)
