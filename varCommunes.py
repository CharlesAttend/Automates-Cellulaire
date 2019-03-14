# -*- coding: utf-8 -*-

class varGlobales():  # Classe stockant quelques 'variables'/constantes pour eviter les conflits de valeurs entre les fichiers

    def __init__(self):  # Constructeur permettant de definir les differents attributs de la classe
        self.hauteurFenetre = 0
        self.largeurFenetre = 0
        self.nbCellules = 0  # Nombre de cellules

        self.nomCsv  = 'csv.csv'  # Nom du csv permettant la generation du csv

        self.departFeu = [0, 0]  # Coordonnees de depart du feu [x, y]

        # Retourne les différents nom des textures
        self.textureArbre  = 'textures\arbre.png'
        self.textureSol = 'textures\sol.png'
        self.textureEau = 'textures\eau.png'
        self.textureArbreBrule = 'textures\arbreBrule.png'
        self.textureArbreEnFeu = 'textures\arbreEnFeu.png'

    # Fonctions dites "Accesseurs", elles retournent les valeurs des differents attributs de la classe

    def getHauteur(self):
        return self.hauteurFenetre
    def getLargeur(self):
        return self.largeurFenetre
    def getNbCellules(self):
        return self.nbCellules
    def getNomCsv(self):
        return self.nomCsv
    def getTexturesName(self):
        return (self.textureArbre, self.textureArbreBrule, self.textureArbreEnFeu, self.textureEau, self.textureSol)


    # Fonctions dites "Mutateurs", elles permettent de modifier les valeurs des differents attributs de la classe

    def setCoordDepartFeu(self, x, y):
        self.departFeu[0] = x
        self.departFeu[1] = y
    def setLargeur(self, largeur):
        self.largeurFenetre = largeur
    def setHauteur(self, hauteur):
        self.hauteurFenetre = hauteur 
    def setNbCell(self, nb):
        self.nbCellules = nb
