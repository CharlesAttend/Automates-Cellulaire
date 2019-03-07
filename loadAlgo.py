# -*- coding: utf-8 -*-

class loadAlgo():
    def __init__ (self):
        self.listeForet = []
        self.listeCellulesEnFeu = []
        self.cellUpdated = 0

    # Fonctions dites "Accesseurs", elles retournent les valeurs des differents attributs de la classe

    def getListeForet(self):
        return list(self.listeForet)

    def getCellEnFeu(self):
        return list(listeCellulesEnFeu)

    def getCellUpdated(self):
        return self.cellUpdated

    # Fonctions dites "Mutateurs", elles permettent de modifier les valeurs des differents attributs de la classe

    def setArbreABruler(self, liste):
        self.listeForet = list(liste)

    def augmentCellUpdated(self):
        self.cellUpdated += 2

    def augmentCellEnFeu(self, x, y):
        self.listeCellulesEnFeu.append(x)
        self.listeCellulesEnFeu.append(y)
