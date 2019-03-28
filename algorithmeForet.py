# -*- coding: utf-8 -*-

####################################################################################################

def propagationFeu(nbCellLignes, cellulesToCheck, foret, currentCell):                # Fonction permettant la propagation du feu,
                                                                 #prend en paramèrts le nb de cellules sur une ligne, une liste contenant les coordonnées de l'arbre en feu et une grill au format du .csv
    cellToCheck  = list(cellulesToCheck)
    listeForet = list(foret)
    listeCellEnFeu = []
    xMin, xMax, yMin, yMax = 0, 0, 0, 0


    if(cellToCheck[currentCell] == 1):
        xMin = cellToCheck[currentCell]-1
        xMax = cellToCheck[currentCell]+1

    elif(cellToCheck[currentCell] == nbCellLignes):
        xMin = cellToCheck[currentCell]-1
        xMax = cellToCheck[currentCell]

    else:
        xMin = cellToCheck[currentCell]-1
        xMax = cellToCheck[currentCell]

    if(cellToCheck[currentCell+1] == 1):
        yMin = cellToCheck[currentCell+1]-1
        yMax = cellToCheck[currentCell+1]+1

    elif(cellToCheck[currentCell+1] == nbCellLignes):
        yMin = cellToCheck[currentCell+1]-1
        yMax = cellToCheck[currentCell+1]

    else:
        yMin = cellToCheck[currentCell+1]-1
        yMax = cellToCheck[currentCell+1]+1

    print("xMin:xMax",xMin,":",xMax)
    print("yMin:yMax",yMin,":",yMax)

    for j in range(yMin, yMax+1):
        for i in range(xMin, xMax+1):

            if(i != cellToCheck[currentCell] or j != cellToCheck[currentCell+1]):
                print("listeForet[j][i] : ", listeForet[j][i])
                if(listeForet[j][i] == "1"):
                    print("Une cellule voisine est un arbre!")
                    listeCellEnFeu.append(i)
                    listeCellEnFeu.append(j)
                    listeForet[j][i] = "3"
            else:
                print("Central cell : ", i, "; ", j, ", ", listeForet[j][i])
                listeForet[j][i] = "3"
    print("Liste cellules en feu (En Sortie d'algo):  ", list(listeCellEnFeu))
    return list(listeCellEnFeu), list(listeForet)
