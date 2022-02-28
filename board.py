import numpy as np
import csv
from random import randint, randrange


class Board:
    def __init__(self, fileName):
        with open(fileName) as tsv:
            map_array = []
            for column in zip(*[line for line in csv.reader(tsv, delimiter="\t")]):
                map_array.append(column)
        self.map = map_array

    def getRandomCoord(self):
        mX = len(self.map) - 1  #maximum value for X
        mY = len(self.map[0]) - 1
        newPos = (randrange(0, mX), randrange(0, mY))
        return newPos

