# -*- coding: utf-8 -*-

class varGlobales():
    def __init__(self):
        self.hauteurFenetre = 800
        self.largeurFenetre = 800
        self.nbCellulesHauteur = 20
        self.nbCellulesLargeur = 20
        self.nomCsv  = 'csv.csv'
        
    def getHauteur(self):
        return self.hauteurFenetre
    def getLargeur(self):
        return self.largeurFenetre
    def getNbCellulesHauteur(self):
        return self.nbCellulesHauteur
    def getNbCellulesLargeur(self):
        return self.nbCellulesLargeur
    def getNomCsv(self):
        return self.nomCsv