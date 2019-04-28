# -*- coding: utf-8 -*-

###########################################################################################################################################

import csv
import classDialectCsv


###########################################################################################################################################

class varGlobales():  # Classe stockant quelques 'variables'/constantes pour eviter les conflits de valeurs entre les fichiers
                        # On évite ainsi les conflits de valeurs entre les fichiers et les variables de type global
    def __init__(self):  # Constructeur permettant de definir les differents attributs de la classe
        self.hauteurFenetre = 0
        self.largeurFenetre = 0
        self.nbCellules = 0  # Nombre de cellules par lignes
        self.loopCount = 0

        self.nomCsv  = 'csv.csv'  # Nom du csv permettant la generation du csv

        self.listeForet = []
        self.listeCellulesEnFeu = []
        self.listeCellToCheck = []
        self.listeOldCellToCheck = []


    # Fonctions dites "Accesseurs", elles retournent les valeurs des differents attributs de la classe

    def getHauteur(self):
        return self.hauteurFenetre

    def getLargeur(self):
        return self.largeurFenetre

    def getNbCellules(self):
        return self.nbCellules

    def getLengthCell(self):
    	return self.largeurFenetre//self.nbCellules

    def getNomCsv(self):
        return self.nomCsv

    def getLoopCount(self):
        return self.loopCount


    def getListeForet(self):
        return list(self.listeForet)

    def getCellEnFeu(self):
        return list(self.listeCellulesEnFeu)

    def getCellToCheck(self):
        return list(self.listeCellToCheck)

    def getOldCellToCheck(self):
        return list(self.listeOldCellToCheck)

###########################################################################################################################################

    # Fonctions dites "Mutateurs", elles permettent de modifier les valeurs des differents attributs de la classe

    def setLargeur(self, largeur):
        self.largeurFenetre = largeur

    def setHauteur(self, hauteur):
        self.hauteurFenetre = hauteur

    def setNbCell(self, nb):
        self.nbCellules = nb

    def setListeForet(self):    #Transformation du csv.csv en une liste à deux dimensions fonctionnelle et plus rapide d'accès
        with open(self.nomCsv, "r", newline='') as f:
            reader = csv.reader(f, classDialectCsv.Dialect())
            doubleList = []
            for row in reader:
                doubleList.append(row)
            self.listeForet = list(doubleList)

    def augmentLoopCount(self):
        self.loopCount += 1


    def setNewListeForet(self, listeForet):
    	self.listeForet = list(listeForet)

    def setOldCellToCheck(self, listeOldCell):
        self.listeOldCellToCheck = list(listeOldCell) 

    def changeCellEnFeu(self, listeCellEnFeu):
        self.listeCellulesEnFeu = list(listeCellEnFeu)

    def changeCellToCheck(self, listeCellulesToCheck):
        self.listeCellToCheck = list(listeCellulesToCheck)

    def augmentCellEnFeu(self, x, y):
        self.listeCellulesEnFeu.append(x)
        self.listeCellulesEnFeu.append(y)

    def augmentCellToCheck(self, x, y):
        self.listeCellToCheck.append(x)
        self.listeCellToCheck.append(y)

    def augmentOldCellToCheck(self, listOfCell):
        self.listeOldCellToCheck += list(listOfCell)

    def returnCellToCheck(self, index):
        return self.listeCellToCheck[index]

    def emptyCellEnFeu(self):
        self.listeCellulesEnFeu.clear()

    def emptyOldCellToCheck(self):
        self.listeOldCellToCheck.clear()