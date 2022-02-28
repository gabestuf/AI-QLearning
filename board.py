import numpy as np
import csv
from random import randint


class Board:
    def __init__(self, fileName):
        with open(fileName) as tsv:
            map_array = []
            for column in zip(*[line for line in csv.reader(tsv, delimiter="\t")]):
                map_array.append(column)
        self.map = map_array

    def getRandomCoord(self):
        newPos = ( randint(0, len(self.map)), randint(0, len(self.map[0])) )
        return newPos

