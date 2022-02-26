import numpy as np
import csv


class Board:
    def __init__(self, fileName):
        with open(fileName) as tsv:
            map_array = []
            for column in zip(*[line for line in csv.reader(tsv, delimiter="\t")]):
                map_array.append(column)
        self.map = map_array

    def getxmax(self):
        xmax = np.max(self.map, axis=0)
        return xmax

    def getymax(self):
        ymax = np.max(self.map, axis=1)
        return ymax
