# -*- coding: utf-8 -*-
import csv
from random import randint
import classDialectCsv
import copy

class algoCSV():
    def __init__(self,csvName1, tailleTx1):
        self.csvName = csvName1
        self.tailleTx = tailleTx1

    def csvToList(self):
        with open(self.csvName, "r", newline='') as f:
            reader = csv.reader(f, classDialectCsv.Dialect())
            doubleList = []
            for row in reader:
                doubleList.append(row)
            return doubleList

    def createCsv(self):
        with open(self.csvName, "w", newline='') as f:
            writer = csv.writer(f, classDialectCsv.Dialect())
            for i in range(self.tailleTx):
                writer.writerow([randint(0,1) for j in range(self.tailleTx)])

    def getReader(self):
    	with open(self.csvName, "r", newline='') as f:
    	    reader = csv.reader(f, classDialectCsv.Dialect())
    	    return copy(reader)