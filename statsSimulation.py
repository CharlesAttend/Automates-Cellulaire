# -*- coding: utf-8 -*-

class statsSimulation():  # Classe permettant de connaitre quelques stats sur la simulation
    def __init__(self):
        self.cellulesUpdated = 1  # Nombre de cellules deja mises en feu avant la prochaine update
        self.cellulesEnFeu = 1  # Nombre de cellules en feu
        self.surfaceBrulee = 0  # Surface de foret brulee en m^2 (Chercher surface moyenne arbre au sol)

    def getCellulesUpdated(self):
        return self.cellulesUpdated

    def getCellulesEnFeu(self):
        return self.cellulesEnFeu

    def getSurfaceBrulee(self):
        return self.surfaceBrulee

    def setCellulesUpdated(self):
        self.cellulesUpdated += 1

    def setCellulesEnFeu(self):
        self.cellulesEnFeu += 1

    def setSurfaceBrulee(self):
        self.surfaceBrulee += 1  # Augmenter de la valeur ligne 7 ...