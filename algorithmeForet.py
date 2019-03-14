﻿# -*- coding: utf-8 -*-

####################################################################################################

def propagationFeu(nbCellLignes, cellulesFeu, foret):                # Fonction permettant la propagation du feu,
                                                                     #prend en paramèrts le nb de cellules sur une ligne, une liste contenant les coordonnées de l'arbre en feu et une grill au format du .csv

    cellEnFeu = list(cellulesFeu)
    listeForet = list(foret)
    minX, maxX, minY, maxY = 0, 0, 0, 0

    for i in range(0, len(cellEnFeu), 2):     # On pacours la liste de 2 en 2 car les coordonnées sont stockées de cette maniere : [X_n, Y_n]
        if(cellEnFeu[i] == 0):                # (début) Test de la position du feu
            minX = cellEnFeu[i]
            maxX = cellEnFeu[i] + 1
            if(cellEnFeu[i+1] == 0):
                minY = cellEnFeu[i+1]
                maxY = cellEnFeu[i+1]+1
            elif(cellEnFeu[i+1] == nbCellLignes):
                minY = cellEnFeu[i+1]-1
                maxY = cellEnFeu[i+1]
        elif(cellEnFeu[i] == nbCellLignes):
            minX = cellEnFeu[i]-1
            maxX = cellEnFeu[i]
            if (cellEnFeu[i+1] == 0):
                minY = cellEnFeu[i+1]
                maxY = cellEnFeu[i+1]+1
            elif (cellEnFeu[i+1] == nbCellLignes):
                minY = cellEnFeu[i+1] - 1
                maxY = cellEnFeu[i+1]
        else:
            minX = cellEnFeu[i]-1
            maxX = cellEnFeu[i]+1
            minY = cellEnFeu[i+1]-1
            maxY = cellEnFeu[i+1]+1            # (fin)

        for y in range(minY, maxY, 1):                              # Si les cellules voisines a celle du feu sont des arbres, elles prennent a leur tour feu
            for x in range(minX, maxX, 1):
                if(x != cellEnFeu[i] and y != cellEnFeu[i+1]):  # Condition pour voir si on test la cellule qui est deja en feu
                    if(listeForet[y][x] == 1):                      # Si la ou les cellules voisines a celles du feu sont des arbres, on l'ajoute à la liste des cellules qui prennent feu / en feu
                        cellEnFeu.append(x)
                        cellEnFeu.append(y)
                        listeForet[x][y] = 0
        return list(cellEnFeu), list(listeForet)


def transformationCsvListe(nbCell, listeForet):   # Fonction convertissant le csv en une liste a deux dimensions de nombres entiers
    csvForet = open("foret.csv", "r") # Csv permettant de generer la foret
    liste = []
    for i in range(nbCell):           # Nombre de cellules en hauteur
        tmp = []
        for j in list(csvForet.readline()):
            if (j != "\n"):
                tmp.append(int(j))
        liste.append(tmp.copy())
        tmp.clear()
    csvForet.close()
    return liste