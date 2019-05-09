# -*- coding: utf-8 -*-

################################################################################################################################################################

from random import randint

################################################################################################################################################################

def propagationFeu(nbCellLignes, x, y, foret): # Algorithme gérant la propagation du feu

    clicX, clicY = x, y # On récupère les coordonnées de la cellule par rapport à la double-liste forêt
    listeForet = list(foret)
    listeCellEnFeu = []   # Liste retournée par la fonction, elle contient les coordonnées dans la double-liste forêt des cellules où le feu va se propager
    xMin, xMax, yMin, yMax = 0, 0, 0, 0

    if(clicX == 0):
        xMin = clicX
        xMax = clicX+1

    elif(clicX == nbCellLignes-1):
        xMin = clicX-1
        xMax = clicX

    else:
        xMin = clicX-1
        xMax = clicX+1

    if(clicY == 0):
        yMin = clicY
        yMax = clicY+1

    elif(clicY == nbCellLignes-1):
        yMin = clicY-1
        yMax = clicY

    else:
        yMin = clicY-1
        yMax = clicY+1

    for j in range(yMin, yMax+1):
        for i in range(xMin, xMax+1):

            if(i != clicX or j != clicY): # Si la cellule à tester est la cellule déjà en feu, on ne fait rien
                if(listeForet[j][i] == "1" and randint(0, 100) < 45): # Si la cellule voisine est un arbre, alors on l'ajoute dans la liste des cellules à incendier
                    listeCellEnFeu.append(i)
                    listeCellEnFeu.append(j)
                    listeForet[j][i] = "3"   # Comme la cellule est un arbre qui va prendre feu, alors on le met à l'état 3, soit arbres en feu

    return list(listeCellEnFeu), list(listeForet)