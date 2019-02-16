# -*- coding: utf-8 -*-

class varGlobales():  # Classe stockant quelques 'variables'/constantes pour eviter les conflits de valeurs entre les fichiers

    def __init__(self):  # Constructeur permettant de definir les differents attributs de la classe
        self.hauteurFenetre = 800
        self.largeurFenetre = 800
        self.nbCellulesHauteur = 20  # Nombre de cellules en hauteur
        self.nbCellulesLargeur = 20  # Nombre de cellules en largeur
        self.nomCsv  = 'csv.csv'  # Nom du csv permettant la generation du csv

    # Fonctions dites "Accesseurs", elles retournent les valeurs des differents attributs de la classe
        
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
