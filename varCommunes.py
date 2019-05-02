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
        self.nbCellules = 0  # Nombre de cellules par lignes<<<<<<< HEAD
        self.burnedTrees = 0 # Nombre d'arbre brûlés
        self.TTtree = 0      # Nombre d'arbres aux débuts de la simulation

        self.nomCsv  = 'csv.csv'  # Nom du csv permettant la generation du csv

        self.listeForet = []
        self.listeCellulesEnFeu = []
        self.listeCellToCheck = []
        self.listeBurnedCell = []

###########################################################################################################################################

    # Fonctions dites "Accesseurs", elles retournent les valeurs des differents attributs de la classe

    def getTTtree(self):
        return self.TTtree

    def getTTtree(self):
        return self.TTtree

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

    def getBurnedTrees(self):
        return self.burnedTrees


    def getListeForet(self):
        return list(self.listeForet)

    def getCellEnFeu(self):
        return list(self.listeCellulesEnFeu)

    def getCellToCheck(self):
        return list(self.listeCellToCheck)

    def getBurnedCell(self):
        return list(self.listeBurnedCell)

###########################################################################################################################################

    # Fonctions dites "Mutateurs", elles permettent de modifier les valeurs des differents attributs de la classe

    def setTTtree(self, tree):
        self.TTtree = tree
        
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

    def augmentBurnedTrees(self, burnedCell):
        self.burnedTrees += burnedCell


    def setNewListeForet(self, listeForet):
        self.listeForet = list(listeForet)

    def setBurnedCell(self, listeOldCell):
        self.listeBurnedCell = list(listeOldCell)

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

    def augmentBurnedCell(self, listOfCell):
        self.listeBurnedCell += list(listOfCell)

    def returnCellToCheck(self, index):
        return self.listeCellToCheck[index]

    def emptyCellEnFeu(self):
        self.listeCellulesEnFeu.clear()

    def emptyBurnedCell(self):
        self.listeBurnedCell.clear()