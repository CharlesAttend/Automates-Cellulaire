# -*- coding: utf-8 -*-

# Projet d'ISN - (2018-2019) - Simulation d'un feu de forêt (Automates Cellulaires)
# Réalisé par Viard Augustin, Vin Charles et Hubinet Benjamin

##################################################################################################################################################

from os import system

def bootstrap():                                # Update les bibliothèques importantes
    system("python -m pip install -U pip")
    system("python -m pip install -U pillow")
# bootstrap()

from tkinter import *
from PIL import Image, ImageTk,Image
from math import ceil
import time
import tkinter.messagebox
import tkinter.filedialog

import AlgoCSV as AC  # ALGOCSV permet de générer un csv en fonction du nombre de cellules choisies par l'utilisateur
import varCommunes as VC  # varCommunes contient une classe qui rassemble toutes les variables utiles aux différents fichiers
import algorithmeForet as algoForet  # Fichier qui contient l'algorithme
import csv
import classDialectCsv

##################################################################################################################################################

 # Chronomètre, permettant d'obtenir des stats en fin de simulation

def lancer_chrono():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge()

def stoper_chrono():
    global flag
    flag=0

def top_horloge():
    global depart,flag
    y = time.time()-depart
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if(flag):
        message.configure(text = "%i min %i sec " %(minutes,secondes))
    Fenetre.after(250,top_horloge)

 # Fin des Fonctions dédiées au chrono

def stats():
    pourcent = (100*vg.getBurnedTrees())//(vg.getTTtree())
    resultat.configure(text = str(pourcent) + "%")

def Clic(event):
    vg.setListeForet()                          # On crée la listeForet à partir du CSV
    listeForet = list(vg.getListeForet())
    X = event.x
    Y = event.y
    X = ceil(X/vg.getLengthCell())-1
    Y = ceil(Y/vg.getLengthCell())-1
    print("Coords:  ", X, ", ", Y)

    if(listeForet[Y][X] != "1"): return False   # On test si la cellule sur laquelle on a cliqué est un arbre, si oui on le met en feu sinon, il ne se passe rien

    vg.augmentCellToCheck(X, Y)
    vg.augmentCellEnFeu(X, Y)
    listeForet[Y][X] = "3"
    vg.setNewListeForet(listeForet)
    updateCoolMap(vg.getCellEnFeu(), [])
    vg.augmentBurnedCell(vg.getCellEnFeu())
    vg.augmentBurnedTrees(1)
    vg.emptyCellEnFeu()

def enregistrer():                              # Fonction permettant de prendre une capture d'écran de la simulation, ainsi que de l'enregistrer
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    image = Image.grab((x+2, y+2, x+w-2, y+h-2))
    image.save("resulat_simulation.png")

def dix():
    vg.setNbCell(10)
    refreshTxPath()

def cinquante():
    vg.setNbCell(50)
    refreshTxPath()

def cent():
    vg.setNbCell(100)
    refreshTxPath()

def refreshTxPath():                            # Réactualise l'emplacement des Textures après un changement de taille
    global grass, tree, water, burningTree, burningGrass, burnedTree, burnedGrass, tailleImg
    tailleImg = vg.getLengthCell()
    grass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/grass.png"))
    tree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/tree.png"))
    water = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/water.png"))
    burningTree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burning_tree.png"))
    burnedTree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burned_tree.png"))
    burningGrass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burning_tree.png"))
    burnedGrass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burned_grass.png"))

# Déroulement de l'algorithme :

def sim_auto():
    updateCoolMap([], vg.getBurnedCell())
    for i in range(0, len(vg.getCellToCheck()), 2):
        tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.returnCellToCheck(i), vg.returnCellToCheck(i+1), vg.getListeForet()) #On test d'abord si le feu peut se propager
        vg.setNewListeForet(tmpListeForet)

        for j in range(0, len(tmpCellEnFeu), 2):
            vg.augmentCellEnFeu(tmpCellEnFeu[j], tmpCellEnFeu[j+1])

    cellEnFeu = list(vg.getCellEnFeu())
    vg.changeCellToCheck(list(cellEnFeu))

    if(len(cellEnFeu) > 0):
        updateCoolMap(cellEnFeu, vg.getBurnedCell())    # On affiche les nouveaux arbres à brûler si  il y en a

    vg.setBurnedCell(list(cellEnFeu))
    vg.augmentBurnedTrees(len(cellEnFeu)//2)
    vg.emptyCellEnFeu()
    canvas.after(100, sim_auto)
    #lancer_chrono()

def pasapas():
    updateCoolMap([], vg.getBurnedCell())
    for i in range(0, len(vg.getCellToCheck()), 2):
        tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.returnCellToCheck(i), vg.returnCellToCheck(i+1), vg.getListeForet()) #On test d'abord si le feu peut se propager
        vg.setNewListeForet(tmpListeForet)

        for j in range(0, len(tmpCellEnFeu), 2):
            vg.augmentCellEnFeu(tmpCellEnFeu[j], tmpCellEnFeu[j+1])

    cellEnFeu = list(vg.getCellEnFeu())
    vg.changeCellToCheck(list(cellEnFeu))

    if(len(cellEnFeu) > 0):
        updateCoolMap(cellEnFeu, vg.getBurnedCell())                    # On affiche les nouveaux arbres à brûler si  il y en a

    vg.setBurnedCell(list(cellEnFeu))
    vg.augmentBurnedTrees(len(cellEnFeu)//2)
    vg.emptyCellEnFeu()

# Fin des fonctions concernant l'algorithme

def updateProMap(cellEnFeu):
    pass
def createProMap():
    pass

def updateCoolMap(cellEnFeu, burnedCell):
    for i in range(0, len(cellEnFeu), 2):
        canvas.itemconfigure(str(cellEnFeu[i])+","+str(cellEnFeu[i+1]), image=burningTree)
    for i in range(0, len(burnedCell), 2):
        canvas.itemconfigure(str(burnedCell[i])+","+str(burnedCell[i+1]), image=burnedTree)
    stats()

def createCoolMap(event):
    algocvs.createCsv()
    cordY = 0
    gridY = 0
    totalTree = 0
    with open("csv.csv", "r", newline='') as f:
        canvas.delete("all")                                # Reset du canvas précédent
        reader = csv.reader(f, classDialectCsv.Dialect())
        for row in reader:                                  # On regarde d'abord les lignes
            cordX = 0                                       # On reset X à chaque nouvelle ligne
            gridX = 0
            for i in row:                                   # Ici c'est la boucle des collones || On met la valeur de la case dans i
                i = int(i)                                  # Mon reader renvoie un i sous forme de String donc je le converti
                #On test le i, 0=grass, 1=tree
                if i == 1:
                    canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=tree, tag=str(gridX)+","+str(gridY))
                    totalTree += 1
                elif i == 0:
                    canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=grass, tag=str(gridX)+","+str(gridY))
                else:
                    canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=water, tag=str(gridX)+","+str(gridY))
                cordX = cordX+tailleImg                     # On augmente les cords pour afficher l'image au bon endroit après
                gridX+=1
            cordY = cordY+tailleImg
            gridY+=1
            vg.setTTtree(totalTree)

##################################################################################################################################################

vg = VC.varGlobales(800, 800, 50) # vg est une instance de varGlobales

algocvs = AC.algoCSV(vg.getNomCsv(), vg.getNbCellules())

vg.setListeForet()

Fenetre = Tk()
Fenetre.title("Fenetre de simulation")
Fenetre.geometry('1000x1000')
canvas = Canvas(Fenetre, width = vg.getLargeur(), height = vg.getHauteur(), background='grey')
menubar = Menu(Fenetre)

menufichier = Menu(menubar, tearoff = 0)
dimensions = Menu(menubar, tearoff = 0)
menufichier.add_command(label = "Enregistrer l'image", command = enregistrer)
menufichier.add_command(label = "Quitter", command = Fenetre.destroy)
dimensions.add_command(label = "10x10", command = dix)
dimensions.add_command(label = "50x50", command = cinquante)
dimensions.add_command(label = "100x100", command = cent)
menubar.add_cascade(label = "Fichier", menu = menufichier)
menubar.add_cascade(label = "Dimensions", menu = dimensions)

resultat = Label(Fenetre, text = "")
auto = Button(Fenetre, text = "Simulation Automatique", bg = "green", command = sim_auto)
manuel = Button(Fenetre, text = "Simulation Pas à Pas", bg = "blue", command = pasapas)
reset = Button(Fenetre, text = "Reset", bg = "red", command = reset)

auto.grid(row = 0, column = 0, sticky = "n")
manuel.grid(row = 1, column = 0, sticky = "n")
reset.grid(row = 2, column = 0, sticky = "n")
resultat.grid(row = 0, column = 2, sticky = "n")

canvas.bind("<Button-1>", Clic)
canvas.bind("<Button-3>", createCoolMap)

# Affichage du menu
Fenetre.config(menu = menubar)

# Utilisation d'un dictionnaire pour conserver une référence
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
gifdict = {}

# Définition des textures en dehors des fonctions (pour eviter de Fenetre.mainloop()):
tailleImg = vg.getLengthCell()
grass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/grass.png"))
tree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/tree.png"))
water = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/water.png"))
burningTree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burning_tree.png"))
burnedTree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burned_tree.png"))
burningGrass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burning_tree.png"))
burnedGrass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burned_grass.png"))

Fenetre.mainloop()
