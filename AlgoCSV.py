# -*- coding: utf-8 -*-
import csv
from random import randint
import classDialectCsv

hauteur = 1000
largeur = 1000
tailleTx = 100
with open("csv.csv", "w") as f:
    #reader = csv.reader(f, dialect())
    writer = csv.writer(f, classDialectCsv.Dialect)
    for i in range(hauteur//tailleTx):
        writer.writerow([randint(0,1) for j in range(largeur//tailleTx)])
    f.close()