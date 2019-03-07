# -*- coding: utf-8 -*-

####################################################################################################

def propagationFeu():                           # Fonction permettant la propagation du feu
    minX, maxX, minY, maxY = 0, 0, 0, 0

    for i in range(0, len(cellulesFeu), 2):     # On pacours la liste de 2 en 2 car les coordonnées sont stockées de cette maniere : [X_n, Y_n]
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

        for y in range(minY, maxY, 1):                              # Si les cellules voisines a celle du feu sont des arbres, elles prennent a leur tour feu
            for x in range(minX, maxX, 1):
                if(x != cellulesFeu[i] and y != cellulesFeu[i+1]):  # Condition pour voir si on test la cellule qui est deja en feu
                    if(listeForet[y][x] == 1):                      # Si la ou les cellules voisines a celles du feu sont des arbres, on l'ajoute à la liste des cellules qui prennent feu / en feu
                        cellulesFeu.append(x)
                        cellulesFeu.append(y)
                        nbCellulesFeu = len(cellulesFeu) / 2


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

def setCoordDepart(x, y):
    cellulesFeu.append(x)
    cellulesFeu.append(y)