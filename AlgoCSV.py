# -*- coding: utf-8 -*-
import csv
from random import random, randint
import classDialectCsv
import copy

class algoCSV():
    def __init__(self, csvName1, nbCellule1):
        self.csvName = csvName1
        self.nbCellule = nbCellule1

    def csvToList(self):
        with open(self.csvName, "r", newline='') as f:
            reader = csv.reader(f, classDialectCsv.Dialect())
            doubleList = []
            for row in reader:
                doubleList.append(row)
            return doubleList

    def createCsv(self):
        doubleListe = self.genList()
        with open(self.csvName, "w", newline='') as f:
            writer = csv.writer(f, classDialectCsv.Dialect())
            for i in range(self.nbCellule):
                writer.writerow(doubleListe[i]) #[randint(0,2) for j in range(self.nbCellule)]
    
    def genList(self):
        doubleListe = []
        for i in range(self.nbCellule):
            listX = []
            for j in range(self.nbCellule):
                nb = random()
                if nb < 0.75:
                    listX.append(1)
                elif nb < 0.97:
                    listX.append(0)
                else:
                    listX.append(2)
            doubleListe.append(listX)
        return doubleListe

    #Water = 5%
    #Tree = 70%
    #Grass = 25%