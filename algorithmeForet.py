# -*- coding: utf-8 -*-

####################################################################################################

def propagationFeu(nbCellLignes, x, y, foret):                # Fonction permettant la propagation du feu,
                                                                 #prend en paramèrts le nb de cellules sur une ligne, une liste contenant les coordonnées de l'arbre en feu et une grill au format du .csv
    clicX, clicY = x, y
    listeForet = list(foret)
    listeCellEnFeu = []
    xMin, xMax, yMin, yMax = 0, 0, 0, 0

    if(clicX == 0):
        xMin = clicX
        xMax = clicX+1

    elif(clicX == nbCellLignes):
        xMin = clicX-1
        xMax = clicX-1

    else:
        xMin = clicX-1
        xMax = clicX+1

    if(clicY == 0):
        yMin = clicY
        yMax = clicY+1

    elif(clicY == nbCellLignes):
        yMin = clicY-1
        yMax = clicY-1

    else:
        yMin = clicY-1
        yMax = clicY+1

    #print("xMin:xMax",xMin,":",xMax)
    #print("yMin:yMax",yMin,":",yMax)

    for j in range(yMin, yMax+1):
        for i in range(xMin, xMax+1):

            if(i != clicX or j != clicY):
                #print("i : ", i, "j : ", j, ", Valeur dans la liste foret : ", listeForet[j][i])
                if(listeForet[j][i] == "1"):
                    listeCellEnFeu.append(i)
                    listeCellEnFeu.append(j)
                    listeForet[j][i] = "3"

return list(listeCellEnFeu), list(listeForet)