# -*- coding: utf-8 -*-

from varCommunes import getLargeurFen, getHauteurFen, getNbCellulesLargeur, getNbCellulesHauteur

####################################################################################################

def posFeuATester(posFeuX, posFeuY, largeurFeu, hauteurFeu, largeurFenetre, hauteurFenetre):        #Test des positions où le feu pourrait se propager
    cellulesATester = []
    for i in range(3):      #Création d'une liste à deux dimension de [3, 3] où le feu serait placé au milieu et les 8 autres cellules seraient les cellules à tester pour voir ou le feu se proprage
        cellulesATester.append([0]*3)

    if(posFeuX == 0):       #Si le feu est dans les coins de la grille en haut à gauche ou en bas à gauche
        if(posFeuY == 0):
            cellulesATester[1][2] = 1
            cellulesATester[2][1] = 1
            cellulesATester[2][2] = 1
        elif(posFeuY == hauteurFenetre - hauteurFeu):
            cellulesATester[0][1] = 1
            cellulesATester[0][2] = 1
            cellulesATester[1][2] = 1
        else:
            cellulesATester[0][1]=1
            cellulesATester[0][2]=1
            cellulesATester[1][2]=1
            cellulesATester[2][1]=1
            cellulesATester[2][2]=1
    elif(posFeuX == largeurFenetre - largeurFeu):       #Si le feu est dans les coins de la grille en haut ou en bas à droite
        if(posFeuY == 0):
            cellulesATester[1][0] = 1
            cellulesATester[2][0] = 1
            cellulesATester[2][1] = 1
        elif(posFeuY == hauteurFenetre - hauteurFeu):
            cellulesATester[0][0] = 1
            cellulesATester[0][1] = 1
            cellulesATester[1][0] = 1
        else:
            cellulesATester[0][1]=1
            cellulesATester[0][2]=1
            cellulesATester[1][0]=1
            cellulesATester[2][0]=1
            cellulesATester[2][1]=1
    elif(posFeuY == 0):
        cellulesATester[0][1]=1
        cellulesATester[0][2]=1
        cellulesATester[1][0]=1
        cellulesATester[2][0]=1
        cellulesATester[2][1]=1
    elif(posFeuY == hauteurFenetre - hauteurFeu):
        cellulesATester[0][0]=1
        cellulesATester[0][1]=1
        cellulesATester[0][2]=1
        cellulesATester[1][0]=1
        cellulesATester[1][2]=1
    else:
        for i in range(3):
            for j in range(3):
                cellulesATester[i][j] = 1
        cellulesATester[1][1] = 0         #Le feu est au milieu de la grille donc cette cellule n'est pas à tester
    return cellulesATester
####################################################################################################
largeurFen, hauteurFen = int(getLargeurFen()), int(getHauteurFen())         #Affectation de variables communes à tout les fichiers et utiles
nbCellulesLargeur, nbCellulesHauteur = int(getNbCellulesLargeur()), int(getNbCellulesHauteur())

#csvForet = open("csv.csv", "r")         #Ouverture du CSV contenant les éléments de la forêt
tabForet = []
for i in range(40): #Création de la liste à deux dimensions à la taille du CSV
    tabForet.append([0] * 40)


print(posFeuATester(760, 0, 40, 40, largeurFen, hauteurFen))