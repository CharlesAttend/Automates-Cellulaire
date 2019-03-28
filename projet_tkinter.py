# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk,Image
from math import ceil
import tkinter.messagebox
import tkinter.filedialog
import AlgoCSV as AC  #ALGOCSV permet de générer un csv en fonction du nombre de cellules choisies par l'utilisateur
import varCommunes as VC  #varCommunes contient une classe qui rassemble toutes les variables utiles aux différents fichiers
import algorithmeForet as algoForet  #Fichier qui contient l'algorithme
import csv
import classDialectCsv

def Clic(event):
    X = event.x
    Y = event.y
    X = ceil(X/vg.getLengthCell())
    Y = ceil(Y/vg.getLengthCell())
    print(vg.getLengthCell())
    vg.augmentCellEnFeu(X, Y)
    vg.augmentCellToCheck(X, Y)
    print(vg.getCellToCheck())
    print(vg.getCellEnFeu())
    vg.setListeForet()

def enregistrer():
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    image = Image.grab((x + 2, y + 2, x + w - 2, y + h - 2))
    image.save("resulat_simulation.png")

def dix () :
    vg.setNbCell(10)

def cinquante () :
    vg.setNbCell(50)

def cent () :
    vg.setNbCell(100)

# Déroulement de l'algorithme :

def sim_auto():
    for i in range(vg.getCurrentCell(), len(vg.getCellToCheck())//2):
        tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.getCellToCheck(), vg.getListeForet(), vg.getCurrentCell()) #On test d'abord si le feu peut se propager
        vg.setNewListeForet(tmpListeForet)

        for j in range(0, len(tmpCellEnFeu), 2):                              #On ajoute tout les arbres a bruler dans la liste cellEnFeu
            vg.augmentCellEnFeu(tmpCellEnFeu[j], tmpCellEnFeu[j+1])

        vg.augmentCurrentCell()
        print("tmpCellEnFeu : ", tmpCellEnFeu)

    cellEnFeu = vg.getCellEnFeu()
    for i in range(0, len(cellEnFeu), 2):
        vg.augmentCellToCheck(cellEnFeu[i], cellEnFeu[i+1])

    if(len(cellEnFeu) > 0):
        for i in range(0, len(vg.getCellEnFeu()), 2):
            updateMap(cellEnFeu)
            #On affiche les nouveaux arbres à brûler
            

    vg.augmentCellUpdated()
    vg.emptyCellEnFeu()
    vg.augmentLoopCount()
    print("executed!")
    canvas.after(2000, sim_auto)

def pasapas():
    for i in range(vg.getCurrentCell(), len(vg.getCellToCheck())//2):
        tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.getCellToCheck(), vg.getListeForet(), vg.getCurrentCell()) #On test d'abord si le feu peut se propager
        vg.setNewListeForet(tmpListeForet)

        for j in range(0, len(tmpCellEnFeu), 2):                              #On ajoute tout les arbres a bruler dans la liste cellEnFeu
            vg.augmentCellEnFeu(tmpCellEnFeu[j], tmpCellEnFeu[j+1])

        vg.augmentCurrentCell()
        print(tmpCellEnFeu)

    cellEnFeu = vg.getCellEnFeu()
    for i in range(0, len(cellEnFeu), 2):
        vg.augmentCellToCheck(cellEnFeu[i], cellEnFeu[i+1])

    if(len(cellEnFeu) > 0):
        for i in range(0, len(vg.getCellEnFeu()), 2):
            #On affiche les nouveaux arbres à brûler
            pass

    vg.augmentCellUpdated()
    vg.emptyCellEnFeu()
    vg.augmentLoopCount()
    print("executed!")

# Fin des fonctions concernant l'algorithme


def drawGrid(): #Fonction qui dessine une grille sur le Canvas pour tester la position des textures
    for i in range(0, 800, 800//vg.getNbCellules()):
        canvas.create_line(0, i, 800, i)
        canvas.create_line(i, 0, i, 800)

def updateMap(cellEnFeu):
    #for i in range()
    print("ye")

def createMap(event):
    algocvs.createCsv()
    grass = ImageTk.PhotoImage(Image.open("textures/grass80x80.png"))
    tree = ImageTk.PhotoImage(Image.open("textures/tree80x80.png"))
    cordY = 0
    tailleImg = vg.getLengthCell()
    with open("csv.csv", "r", newline='') as f:
        reader = csv.reader(f, classDialectCsv.Dialect())
        for row in reader:                                  #On regarde d'abord les lignes
            cordX = 0                                       #On reset X à chaque nouvelle ligne
            for i in row:                                   #Ici c'est la boucle des collones || On met la valeur de la case dans i
                i = int(i)                                  #Mon reader renvoie un i sous forme de String donc je le converti
                #On test le i, 0=grass, 1=tree
                if i == 0:  
                    canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=grass)
                elif i == 1:
                    canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=tree)
                cordX = cordX+tailleImg                     #On augmente les cords pour afficher l'image au bon endroit après
            cordY = cordY+tailleImg
    Fenetre.mainloop()

vg = VC.varGlobales() #vg est une instance de varGlobales
vg.setLargeur(800)
vg.setHauteur(800)
vg.setNbCell(10)

algocvs = AC.algoCSV(vg.getNomCsv(), vg.getNbCellules())

Fenetre = Tk()
Fenetre.title("Fenetre de simulation")
Fenetre.geometry('1000x1000')
canvas = Canvas(Fenetre, width = 800, height = 800, background='grey')
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

auto = Button(Fenetre, text = "Simulation Automatique", bg = "green", command = sim_auto)
manuel = Button(Fenetre, text = "Simulation Pas à Pas", bg = "blue", command = pasapas)
auto.grid(row = 0, column = 0, sticky = "n")
manuel.grid(row = 1, column = 0, sticky = "n")

canvas.bind("<Button-1>", Clic)
#canvas.bind("<Button-3>", drawGrid)
canvas.bind("<Button-3>", createMap)
# Affichage du menu
Fenetre.config(menu = menubar)

# Utilisation d'un dictionnaire pour conserver une référence
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
gifdict = {}
Fenetre.mainloop()