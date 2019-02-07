# -*- coding: utf-8 -*-
import csv
from random import randint
from varCommunes import *


import classDialectCsv
dialect = classDialectCsv.Dialect()
hauteur = getHauteurFen()
largeur = getLargeurFen()
with open(getFileName(), "wb") as f:
    #reader = csv.reader(f, dialect())
    writer = csv.writer(f, classDialectCsv.Dialect)
    for i in range(hauteur):
        writer.writerow([randint(0,1) for j in range(largeur)])
    f.close()