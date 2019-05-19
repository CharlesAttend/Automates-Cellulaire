# -*- coding: utf-8 -*-

# Projet d'ISN - (2018-2019) - Simulation d'un feu de forêt (Automates Cellulaires)
# Réalisé par Viard Augustin, Vin Charles et Hubinet Benjamin

##################################################################################################################################################

from os import system, execl

def bootstrap():                                # Update les bibliothèques importantes
    system("python -m pip install -U pip")
    system("python -m pip install -U pillow")
# bootstrap()

from tkinter import *
from PIL import Image, ImageTk, ImageGrab
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
def reset():
    execl(sys.executable, sys.executable, *sys.argv)                        #Execute l'executable en argument, tout en remplaçant le processus du deuxième argument + les arguments
                                                                            #On reprend donc ici le path du fichier et les arguments

def buttonPlusSimu():
    if not textBoxProba.get() == "":
        vg.setProba(float(textBoxProba.get()))
    lancer_chrono()
    sim_auto()

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
    Fenetre.after(250, top_horloge)
 # Fin des Fonctions dédiées au chrono

def stats():
    pourcent = (100*vg.getBurnedTrees())//(vg.getTTtree())
    resultat.configure(text = str(pourcent) + "%")
    surfaceBrulee.configure(text = str((vg.getBurnedTrees()*4)/10000) + " ha") #On considère que la surface d'un arbre est de 4m²

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
    updateMap(vg.getCellEnFeu(), [])
    vg.augmentBurnedCell(vg.getCellEnFeu())
    vg.augmentBurnedTrees(1)
    vg.emptyCellEnFeu()

def enregistrer():                              # Fonction permettant de prendre une capture d'écran de la simulation, ainsi que de l'enregistrer
    x=canvas.winfo_rootx()
    y=canvas.winfo_rooty()
    w=canvas.winfo_width()
    h=canvas.winfo_height()
    image=ImageGrab.grab((x-175,y-50,x+w,y+h))
    image.save("Résulat_Simulation.png")

def dix():
    vg.setNbCell(10)
    refreshTxPath()

def cinquante():
    vg.setNbCell(50)
    refreshTxPath()

def refreshTxPath():                                   # Réactualise l'emplacement des Textures après un changement de taille
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
    updateMap([], vg.getBurnedCell())                                   # La cellule mise en feu au départ se transforme en cellule d'abre en cendre
    for i in range(0, len(vg.getCellToCheck()), 2):
        tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.returnCellToCheck(i), vg.returnCellToCheck(i+1), vg.getListeForet(), vg.getProba()) #On test d'abord si le feu peut se propager
        vg.setNewListeForet(tmpListeForet)                              # On modifie la liste contenant la génération de forêt, car si des arbres ont brûlés, la génération a été modifiéé

        for j in range(0, len(tmpCellEnFeu), 2):
            vg.augmentCellEnFeu(tmpCellEnFeu[j], tmpCellEnFeu[j+1])     # On ajoute les coordonnées des nouveaux arbres à brûler si il y en a

    cellEnFeu = list(vg.getCellEnFeu())
    vg.changeCellToCheck(list(cellEnFeu))                               # On affecte la liste des cellules en feu à la liste des cellules sur lesquelles on va tester la propagation du feu au tour prochain

    if(len(cellEnFeu) > 0):
        updateMap(cellEnFeu, vg.getBurnedCell())                           # On affiche les nouveaux arbres à brûler si  il y en a
    else:
        stoper_chrono()

    vg.setBurnedCell(list(cellEnFeu))                                   # On ajoute les cellules en feu à la liste des cellules à mettre en cendre à la prochaine génération
    vg.augmentBurnedTrees(len(cellEnFeu)//2)                            # On ajoute le nombre d'arbre brûlés durant cette génération au compteur d'abres brûlés
    vg.emptyCellEnFeu()                                                 # Comme toutes les cellules ont étés brûlées, on vide la liste des cellules à brûler
    canvas.after(100, sim_auto)

def pasapas():
    updateMap([], vg.getBurnedCell())                                   # La cellule mise en feu au départ se transforme en cellule d'abre en cendre
    for i in range(0, len(vg.getCellToCheck()), 2):
        tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.returnCellToCheck(i), vg.returnCellToCheck(i+1), vg.getListeForet(), vg.getProba()) #On test d'abord si le feu peut se propager
        vg.setNewListeForet(tmpListeForet)                              # On modifie la liste contenant la génération de forêt, car si des arbres ont brûlés, la génération a été modifiéé

        for j in range(0, len(tmpCellEnFeu), 2):
            vg.augmentCellEnFeu(tmpCellEnFeu[j], tmpCellEnFeu[j+1])     # On ajoute les coordonnées des nouveaux arbres à brûler si il y en a

    cellEnFeu = list(vg.getCellEnFeu())
    vg.changeCellToCheck(list(cellEnFeu))                               # On affecte la liste des cellules en feu à la liste des cellules sur lesquelles on va tester la propagation du feu au tour prochain

    if(len(cellEnFeu) > 0):
        updateMap(cellEnFeu, vg.getBurnedCell())                           # On affiche les nouveaux arbres à brûler si  il y en a

    vg.setBurnedCell(list(cellEnFeu))                                   # On ajoute les cellules en feu à la liste des cellules à mettre en cendre à la prochaine génération
    vg.augmentBurnedTrees(len(cellEnFeu)//2)                            # On ajoute le nombre d'arbre brûlés durant cette génération au compteur d'abres brûlés
    vg.emptyCellEnFeu()                                                 # Comme toutes les cellules ont étés brûlées, on vide la liste des cellules à brûler

# Fin des fonctions concernant l'algorithme


def updateMap(cellEnFeu, burnedCell):                               #Ici on update l'affichage par un boucle qui prend une liste de cellule à update
    for i in range(0, len(cellEnFeu), 2):
        canvas.itemconfigure(str(cellEnFeu[i])+","+str(cellEnFeu[i+1]), image=burningTree)
    for i in range(0, len(burnedCell), 2):
        canvas.itemconfigure(str(burnedCell[i])+","+str(burnedCell[i+1]), image=burnedTree)
    stats()

def createMap(event):
    algocsv.createCsv()                                     #On créé un csv
    cordY = 0
    gridY = 0
    totalTree = 0
    with open(vg.getNomCsv(), "r", newline='') as f:
        canvas.delete("all")                                # Reset du canvas précédent
        reader = csv.reader(f, classDialectCsv.Dialect())
        for row in reader:                                  # On regarde d'abord les lignes
            cordX = 0                                       # On reset X à chaque nouvelle ligne
            gridX = 0
            for i in row:                                   # Ici c'est la boucle des collones || On met la valeur de la case dans i
                i = int(i)                                  # Mon reader renvoie un i sous forme de String donc je le converti
                #On test le i, 0=grass, 1=tree, else=eau
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

vg = VC.varGlobales(800, 800, 10) # vg est une instance de varGlobales

algocsv = AC.algoCSV(vg)

vg.setListeForet()

Fenetre = Tk()
Fenetre.title("Fenetre de simulation")
Fenetre.geometry('1500x1000')
canvas = Canvas(Fenetre, width = vg.getLargeur(), height = vg.getHauteur(), background ='white')
menubar = Menu(Fenetre)

menufichier = Menu(menubar, tearoff = 0)
dimensions = Menu(menubar, tearoff = 0)
menufichier.add_command(label = "Enregistrer l'image", command = enregistrer)
menufichier.add_command(label = "Quitter", command = Fenetre.destroy)
dimensions.add_command(label = "10x10", command = dix)
dimensions.add_command(label = "50x50", command = cinquante)
menubar.add_cascade(label = "Fichier", menu = menufichier)
menubar.add_cascade(label = "Dimensions", menu = dimensions)

auto = Button(Fenetre, text = "Simulation Automatique", bg = "green", command = buttonPlusSimu, bd=4)
manuel = Button(Fenetre, text = "Simulation Pas à Pas", bg = "blue", command = pasapas, bd=4)
resetButton = Button(Fenetre, text = "RESET", bg = "red", command = reset, bd=4)
textBoxProba = Entry(Fenetre, justify="center", bd=4)
resultat = Label(Fenetre, text = "")
surfaceBrulee = Label(Fenetre, text = "")
message = Label(Fenetre, text="")

auto.grid(row = 0, column = 0, sticky = "n")
manuel.grid(row = 1, column = 0, sticky = "n")
resetButton.grid(row = 2, column = 0, sticky = "n")
Label(Fenetre, text="Probabilité:").grid(row = 3, column = 0, sticky = "n")
textBoxProba.grid(row = 4, column = 0, sticky = "n")

resultat.grid(row = 0, column = 1, sticky = "n")
surfaceBrulee.grid(row = 0, column = 2, sticky = "n")

message.grid(row = 1, column = 2, sticky = "n")

canvas.bind("<Button-1>", Clic)
canvas.bind("<Button-3>", createMap)

# Affichage du menu
Fenetre.config(menu = menubar)

# Utilisation d'un dictionnaire pour conserver une référence
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Définition des textures en dehors des fonctions (pour eviter de Fenetre.mainloop()):
tailleImg = vg.getLengthCell()
grass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/grass.png"))
tree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/tree.png"))
water = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/water.png"))
burningTree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burning_tree.png"))
burnedTree = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burned_tree.png"))
burningGrass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burning_tree.png"))
burnedGrass = ImageTk.PhotoImage(Image.open("textures/"+str(tailleImg)+"/burned_grass.png"))

flag = 0                                                    #On init flag ici pour pouvoir arreter le chrono dans d'autres fonctions

createMap(0)                                            #On crée un map au démarage 
Fenetre.mainloop()
