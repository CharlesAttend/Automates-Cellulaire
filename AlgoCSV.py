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
        print(doubleList)

hauteur = 1000
largeur = 1000
tailleTx = 100
with open("csv.csv", "w", newline='') as f:
    writer = csv.writer(f, classDialectCsv.Dialect())
    for i in range(hauteur//tailleTx):
        writer.writerow([randint(0,1) for j in range(largeur//tailleTx)])
