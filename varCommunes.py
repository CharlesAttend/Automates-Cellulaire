# -*- coding: utf-8 -*-

class varGlobales(): # Classe permettant aux differents fichiers d'utiliser les memes 'variables'/constantes
    def __init__(self): # Constructeur definissant toutes les 'attributs'/constantes de la classe
        self.hauteurFenetre = 800 
        self.largeurFenetre = 800
        self.nbCellulesHauteur = 20
        self.nbCellulesLargeur = 20 
        self.nomCsv  = 'csv.csv'
    
    # Fonctions dites 'Accesseurs', elles retournent les différents attributs de la classe
    
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
