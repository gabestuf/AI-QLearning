from array import *
import random

from numpy import percentile

'''
You can either hand generate maps or randomly create them.  Generate 10 boards of a size where Heuristic #1 can solve them in approximately 30 seconds.  

For now change variables
num_of_boards 
num_columns 
num_rows 
manually
'''
num_of_boards = 1
num_columns = 50
num_rows = 50
percentOfNonZeros = .01 # float 0-1

def generate_numbers(board_array):
    for x in range(num_columns):
        board_array.append([])
        for y in range(num_rows):
            if (random.randint(0,100)/100 > percentOfNonZeros):
                board_array[x].append(0)
            else:
                board_array[x].append(random.randint(-10, 10))
    return board_array


def remove_end_spaces(string):
    return "".join(string.rstrip())


def board_to_string(board_array):
    board_string = ""
    for x in range(num_columns):
        for y in range(num_rows):
            board_string = board_string + str(board_array[x][y]) + "\t"
        board_string = remove_end_spaces(board_string)
        board_string = board_string + "\n"

    # print(board_string)
    return board_string


def write_board_to_file(file_name, board_string):
    f = open(file_name, "w")
    f.write(board_string)
    f.close()


def main():

    print("Generating_Boards")
    for i in range(num_of_boards):
        board_array = []
        fname = "boards/board"+ str(i + 1)+ ".txt"
        updated_board = generate_numbers(board_array)
        board_string = board_to_string(updated_board)
        write_board_to_file(fname, board_string)


if __name__ == '__main__':
    main()
