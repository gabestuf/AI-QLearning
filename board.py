
import csv


class Board:
    def __init__(self, fileName):
        with open(fileName) as tsv:
            map_array = []
            for column in zip(*[line for line in csv.reader(tsv, delimiter="\t")]):
                map_array.append(column) 
        self.map = map_array



        


    

