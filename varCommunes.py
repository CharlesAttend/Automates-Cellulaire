# -*- coding: utf-8 -*-

class varGlobales():  # Classe stockant quelques 'variables'/constantes pour eviter les conflits de valeurs entre les fichiers

    def __init__(self, hauteur, largeur, nbCellHauteur, nbCellLargeur):  # Constructeur permettant de definir les differents attributs de la classe
        self.hauteurFenetre = hauteur
        self.largeurFenetre = largeur
        self.nbCellulesHauteur = nbCellHauteur  # Nombre de cellules en hauteur
        self.nbCellulesLargeur = nbCellLargeur  # Nombre de cellules en largeur

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
    def getNbCellulesHauteur(self):
        return self.nbCellulesHauteur
    def getNbCellulesLargeur(self):
        return self.nbCellulesLargeur
    def getNomCsv(self):
        return self.nomCsv
    def getTexturesName(self):
        return(self.textureArbre, self.textureArbreBrule, self.textureArbreEnFeu, self.textureEau, self.textureSol)

    # Fonctions dites "Mutateurs", elles permettent de modifier les valeurs des differents attributs de la classe

    def setCoordDepartFeu(self, x, y):
        self.departFeu[0] = x
        self.departFeu[1] = y
