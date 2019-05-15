# -*- coding: utf-8 -*-


#####################################################################################################

import csv
from random import random, randint
import classDialectCsv
import copy

#####################################################################################################

class algoCSV():
    def __init__(self, varglobal):
        self.vg = varglobal

    def createCsv(self):
        doubleListe = self.genList()
        with open(self.vg.getNomCsv(), "w", newline='') as f:
            writer = csv.writer(f, classDialectCsv.Dialect())
            for i in range(self.vg.getNbCellules()):
                writer.writerow(doubleListe[i])
    
    def genList(self):
        doubleListe = []
        for i in range(self.vg.getNbCellules()):
            listX = []
            for j in range(self.vg.getNbCellules()):
                nb = random()
                if nb < 0.75:                   #Abre 75%
                    listX.append(1)
                elif nb < 0.97:                 #Grass 22%
                    listX.append(0)
                else:                           #Eau 3%
                    listX.append(2)
            doubleListe.append(listX)
        return doubleListe
