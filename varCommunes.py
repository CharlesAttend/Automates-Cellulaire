# -*- coding: utf-8 -*-

import csv
import classDialectCsv

class varGlobales():   # Classe stockant quelques 'variables'/constantes
                       # On évite ainsi les conflits de valeurs entre les fichiers et les variables de type global

    def __init__(self):  # Constructeur permettant de definir les differents attributs de la classe
        self.hauteurFenetre = 0

        self.nomCsv  = 'csv.csv'  # Nom du csv permettant la generation du csv

        self.listeForet = []
        self.listeCellulesEnFeu = []
        self.listeOldCellulesEnFeu = []
        self.listeCellToCheck = []    # Liste contenant des cellules de type 'Arbre' où l'on va tester si le feu se propage

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

    def getTexturesName(self):
        return (self.textureArbre, self.textureArbreBrule, self.textureArbreEnFeu, self.textureEau, self.textureSol)



    def getListeForet(self):
        return list(self.listeForet)

    def getCellEnFeu(self):
        return list(self.listeCellulesEnFeu)

    def getCellToCheck(self):
        return list(self.listeCellToCheck)

    # Fonctions dites "Mutateurs", elles permettent de modifier les valeurs des differents attributs de la classe

    def setLargeur(self, largeur):
        self.largeurFenetre = largeur

    def setHauteur(self, hauteur):
        self.hauteurFenetre = hauteur

    def setNbCell(self, nb):
        self.nbCellules = nb

    def setListeForet(self):
        with open(self.nomCsv, "r", newline='') as f:
            reader = csv.reader(f, classDialectCsv.Dialect())
            doubleList = []
            for row in reader:
                doubleList.append(row)
            self.listeForet = list(doubleList)


    def setNewListeForet(self, listeForet):
    	self.listeForet = list(listeForet)

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

    def returnCellToCheck(self, index):
        return self.listeCellToCheck[index]

    def emptyCellEnFeu(self):
        self.listeCellulesEnFeu.clear()
