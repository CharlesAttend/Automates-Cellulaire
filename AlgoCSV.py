# -*- coding: utf-8 -*-
import csv
from random import randint
import classDialectCsv

def csvToList():
    with open("csv.csv", "r", newline='') as f:
        reader = csv.reader(f, classDialectCsv.Dialect())
        doubleList = []
        for row in reader:
            doubleList.append(row)
        return doubleList

def createCsv(hauteur, largeur, tailleTx):
    with open("csv.csv", "w", newline='') as f:
        writer = csv.writer(f, classDialectCsv.Dialect())
        for i in range(hauteur//tailleTx):
            writer.writerow([randint(0,1) for j in range(largeur//tailleTx)])

def getReader():
	with open("csv.csv", "r", newline='') as f:
	    reader = csv.reader(f, classDialectCsv.Dialect())
	    return reader