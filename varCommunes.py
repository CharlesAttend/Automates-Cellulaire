# -*- coding: utf-8 -*-

####################### Accesseurs ###########################

def getLargeurFen():
    return largeur

def getHauteurFen():
    return hauteur

def getNbCellulesLargeur():
    return nbCellulesLargeur

def getNbCellulesHauteur():
    return nbCellulesHauteur

def getPointDepartFeu():
    return (pointDepartX, pointDepartY)

def getFileName():
    return fileName

##############################################################

####################### Variables ############################

largeur, hauteur = 800, 800
nbCellulesLargeur, nbCellulesHauteur = 20, 20 #Nombre de cellules en hauteur et largeur
pointDepartX, pointDepartY = 0, 0       #Point de départ du feu
fileName = "csv.csv"                    #Nom du csv contenant la génération de forêt

##############################################################