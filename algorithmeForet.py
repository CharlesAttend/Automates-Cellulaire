# -*- coding: utf-8 -*-

#import varCommunes

####################################################################################################

def propagationFeu():   # Fonction permettant la propagation du feu
    minX, maxX, minY, maxY = 0, 0, 0, 0
    for i in range(0, len(cellulesFeu), 2):
        if(cellulesFeu[i] == 0):                # (début) Test de la position du feu
            minX = cellulesFeu[i]
            maxX = cellulesFeu[i] + 1
            if(cellulesFeu[i+1] == 0):
                minY = cellulesFeu[i+1]
                maxY = cellulesFeu[i+1]+1
            elif(cellulesFeu[i+1] == 19):
                minY = cellulesFeu[i+1]-1
                maxY = cellulesFeu[i+1]
        elif(cellulesFeu[i] == 19):
            minX = cellulesFeu[i]-1
            maxX = cellulesFeu[i]
            if (cellulesFeu[i+1] == 0):
                minY = cellulesFeu[i+1]
                maxY = cellulesFeu[i+1]+1
            elif (cellulesFeu[i+1] == 19):
                minY = cellulesFeu[i+1] - 1
                maxY = cellulesFeu[i+1]
        else:
            minX = cellulesFeu[i]-1
            maxX = cellulesFeu[i]+1
            minY = cellulesFeu[i+1]-1
            maxY = cellulesFeu[i+1]+1            # (fin)

        for y in range(minY, maxY, 1):  # Si les cellules voisines a celle du feu sont des arbres, elles prennent a leur tour feu
            for x in range(minX, maxX, 1):
                if(x != cellulesFeu[i] and y != cellulesFeu[i+1]):  # Condition pour voir si on test la cellule qui est deja en feu
                    if(listeForet[y][x] == 1):  # Si la ou les cellules voisines a celles du feu sont des arbres, on l'ajoute à la liste des cellules qui prennent feu / en feu
                        cellulesFeu.append(x)
                        cellulesFeu.append(y)
                        nbCellulesFeu = len(cellulesFeu) / 2


def transformationCsvListe():   # Fonction convertissant le csv en une liste a deux dimensions de nombres entiers
    for i in range(20): # Nombre de cellules en hauteur
        tmp = []
        for j in list(csvForet.readline()):
            if (j != "\n"):
                tmp.append(int(j))
        listeForet.append(tmp.copy())
        tmp.clear()

csvForet = open("foret.csv", "r")   # Csv permettant de generer la foret
departFeu = (8, 8)  # Coordonnees X, Y du depart de feu
cellulesFeu = [departFeu[0], departFeu[1]]
nbCellulesFeu = len(cellulesFeu)/2  # Variable permettant de connaitre le nombre de cellules en feu
nbCellulesUpdate = 1 # Nomnbre de cellules qui ont deja ete mises en feu
listeForet = [] # Csv converti en liste d'entiers compris entre 0 : (terre),  1 : (arbres) et 2 : (feu)

transformationCsvListe()
print(listeForet)

csvForet.close()