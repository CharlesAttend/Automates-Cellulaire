# -*- coding: utf-8 -*-

from fenForet import getLargeurFen, getHauteurFen, getNbCellulesLargeur, getNbCellulesHauteur
from genererForet import genererCsv

def copieCsv():
    i = 0
    while(1):
        ligneCsv = csvForet.readline()
        if(ligneCsv == ""):
            break
        tmp = list(ligneCsv)
        del tmp[-1]
        for j in range(40):
            valeur = int(tmp[j])
            tabForet[i][j] = valeur
        tmp.clear()
        i += 1
    csvForet.close()

def getTabForet():
    return tabForet

largeurFen, hauteurFen = int(getLargeurFen()), int(getHauteurFen())
nbCellulesLargeur, nbCellulesHauteur = int(getNbCellulesLargeur()), int(getNbCellulesHauteur())

csvForet = open("foret.csv", "r")
tabForet = []

for i in range(40):
    tabForet.append([0] * 40)

genererCsv()
copieCsv()