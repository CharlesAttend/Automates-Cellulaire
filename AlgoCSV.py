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
    return doubleList

def transformationCsvListe():   # Fonction convertissant le csv en une liste a deux dimensions de nombres entiers
    for i in range(10): # Nombre de cellules en hauteur
        tmp = []
        for j in list(csvForet.readline()):
            if (j != "\n"):
                tmp.append(int(j))
        listeForet.append(tmp.copy())
        tmp.clear()

hauteur = 1000
largeur = 1000
tailleTx = 100
with open("csv.csv", "w", newline='') as f:
    writer = csv.writer(f, classDialectCsv.Dialect())
    for i in range(hauteur//tailleTx):
        writer.writerow([randint(0,1) for j in range(largeur//tailleTx)])

with open("csv.csv", "r", newline='') as f:
    reader = csv.reader(f, classDialectCsv.Dialect())
    doubleList = 0
    #for row in reader:
     #   print(row)

liste = csvToList()
print(liste[2][1])