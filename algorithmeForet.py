# -*- coding: utf-8 -*-

####################################################################################################

def propagationFeu(nbCellLignes, cellulesToCheck, foret, currentCell):                # Fonction permettant la propagation du feu,
                                                                 #prend en paramèrts le nb de cellules sur une ligne, une liste contenant les coordonnées de l'arbre en feu et une grill au format du .csv
    cellToCheck  = list(cellulesToCheck)
    listeForet = list(foret)
    listeCellEnFeu = []
    xMin, xMax, yMin, yMax = 0, 0, 0, 0


    if(cellToCheck[currentCell] == 0):
        xMin = cellToCheck[currentCell]
        xMax = cellToCheck[currentCell]+1

    elif(cellToCheck[currentCell] == nbCellLignes):
        xMin = cellToCheck[currentCell]-1
        xMax = cellToCheck[currentCell]

    else:
        xMin = cellToCheck[currentCell]-1
        xMax = cellToCheck[currentCell]+1

    if(cellToCheck[currentCell+1] == 0):
        yMin = cellToCheck[currentCell+1]
        yMax = cellToCheck[currentCell+1]+1

    elif(cellToCheck[currentCell+1] == nbCellLignes):
        yMin = cellToCheck[currentCell+1]-1
        yMax = cellToCheck[currentCell+1]

    else:
        yMin = cellToCheck[currentCell+1]-1
        yMax = cellToCheck[currentCell+1]-1

    for j in range(yMin, yMax, 1):
        for i in range(xMin, xMax, 1):
            if(i != cellToCheck[currentCell] and j != cellToCheck[currentCell+1]):
                if(listeForet[j][i] == 1):
                    listeCellEnFeu.append(i)
                    listeCellEnFeu.append(j)
                    listeForet[j][i] = 2
            else:
                listeForet[j][i] = 2

    return list(listeCellEnFeu), list(listeForet)
