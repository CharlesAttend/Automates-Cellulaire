# -*- coding: utf-8 -*-

import csv
import classDialectCsv

class varGlobales():  # Classe stockant quelques 'variables'/constantes pour eviter les conflits de valeurs entre les fichiers

    def __init__(self):  # Constructeur permettant de definir les differents attributs de la classe
        self.hauteurFenetre = 0
        self.largeurFenetre = 0
        self.nbCellules = 0  # Nombre de cellules
        self.loopCount = 0

        self.nomCsv  = 'csv.csv'  # Nom du csv permettant la generation du csv

        # Retourne les différents nom des textures
        self.textureArbre  = 'textures/arbre.png'
        self.textureSol = 'textures/grass80x80.png'
        self.textureEau = 'textures/eau.png'
        self.textureArbreBrule = 'textures/arbreBrule.png'
        self.textureArbreEnFeu = 'textures/arbreEnFeu.png'

        self.listeForet = []
        self.listeCellulesEnFeu = []
        self.listeCellToCheck = []
        self.cellUpdated = 0
        self.currentCell = 0


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

    def getLoopCount(self):
        return self.loopCount


    def getListeForet(self):
        return list(self.listeForet)
    def getCellEnFeu(self):
        return list(self.listeCellulesEnFeu)
    def getCellUpdated(self):
    	return self.cellUpdated
    def getCellToCheck(self):
        return list(self.listeCellToCheck)
    def getCurrentCell(self):
        return self.currentCell

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
            print("Liste Foret : ", self.listeForet)

    def augmentLoopCount(self):
        self.loopCount += 1



    def setNewListeForet(self, listeForet):
    	self.listeForet = list(listeForet)

    def augmentCurrentCell(self):
        self.currentCell += 2

    def augmentCellEnFeu(self, x, y):
        self.listeCellulesEnFeu.append(x)
        self.listeCellulesEnFeu.append(y)

    def augmentCellToCheck(self, x, y):
        self.listeCellToCheck.append(x)
        self.listeCellToCheck.append(y)

    def augmentCellUpdated(self):
        self.cellUpdated += 2

    def emptyCellEnFeu(self):
        self.listeCellulesEnFeu.clear()