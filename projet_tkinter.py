# -*- coding: utf-8 -*-

"""
	Attention, si vous voulez interpréter ce code, mettez en commentaire de la ligne 42 à 67 et 76 à 94
"""

from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import tkinter.messagebox
import tkinter.filedialog
import AlgoCSV #ALGOCSV permet de générer un csv en fonction du nombre de cellules choisies par l'utilisateur
import varCommunes as VC #varCommunes contient une classe qui rassemble toutes les variables utiles aux différents fichiers
import algorithmeForet as algoForet #Fichier qui contient l'algorithme

def Clic(event):
    X = event.x
    Y = event.y
    X = int(X/100)*100
    Y = int(Y/100)*100
    loadAlgoForet.augmentCellEnFeu(X, Y)

def enregistrer():
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    image = ImageGrab.grab((x + 2, y + 2, x + w - 2, y + h - 2))
    image.save("resulat_simulation.png")

def dix () :
    vg.setNbCell(10)

def cinquante () :
	vg.setNbCell(50)

def cent () :
	vg.setNbCell(100)


# Déroulement de l'algorithme : 

def sim_auto():
	tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.getCellEnFeu(), vg.getListeForet()) #On test d'abord si le feu peut se propager
																																			#sur les 8 cases autour de l'arbre
	vg.setNewListeForet(tmpListeForet)							#On actualise la liste de la foret
	for i in range(vg.getCellUpdated(),len(tmpCellEnFeu), 2):	#On créer une boucle permettant d'ajouter à la liste des cellules en feu les coordonnées des prochains arbre à brûler
		vg.augmentCellEnFeu(tmpCellEnFeu[i], tmpCellEnFeu[i+1])

	for i in range(vg.getCellUpdated(), len(tmpCellEnFeu), 2):  #On affiche les nouveaux arbres à prendre feu...
		pass 	#...

	vg.augmentCellUpdated(2)
    Fenetre.update()				#On raffraîchit l'écran
    canvas.after(2000, sim_auto)	#On appelle de nouveau la fonction de simulation après 2 secondes

def pasapas():
    tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), vg.getCellEnFeu(), vg.getListeForet()) #On test d'abord si le feu peut se propager
																																			#sur les 8 cases autour de l'arbre
	vg.setNewListeForet(tmpListeForet)							#On actualise la liste de la foret
	for i in range(vg.getCellUpdated(),len(tmpCellEnFeu), 2):	#On créer une boucle permettant d'ajouter à la liste des cellules en feu les coordonnées des prochains arbre à brûler
		vg.augmentCellEnFeu(tmpCellEnFeu[i], tmpCellEnFeu[i+1])

	for i in range(vg.getCellUpdated(), len(tmpCellEnFeu), 2): #On affiche les nouveaux arbres à prendre feu...
		pass 	#...

	vg.augmentCellUpdated(2)
    Fenetre.update()				#On raffraîchit l'écran

# Fin des fonctions concernant l'algorithme

def drawGrid(event): #Fonction qui dessine une grille sur le Canvas pour tester la position des textures
    for i in range(0, 1000, 1000//vg.getNbCellules()):
        canvas.create_line(0, i, 1000, i)
        canvas.create_line(i, 0, i, 1000)

def createMap():
    AlgoCSV.createCsv(vg.getHauteur, vg.getLargeur, vg.getNbCellules)
    reader = AlgoCSV.getReader()
    tailleImg = vg.getNbCellules()
    grass = ImageTk.PhotoImage(Image.open("textures/sol.png"))
    for row in reader:
        for i in row:
            cordX = cordX+tailleImg
            cordY = cordY+tailleImg
            if i == 0:
                canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=grass)



vg = VC.varGlobales() #vg est une instance de varGlobales
vg.setLargeur(1000)
vg.setHauteur(1000)
createmap() #On génère le csv
vg.setListeForet() #On transforme le csv en une liste 2d utilisable pour l'algorithme

Fenetre = Tk()
Fenetre.title("Image")
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
canvas.bind("<Button-3>", drawGrid)
# Affichage du menu
Fenetre.config(menu = menubar)


# Utilisation d'un dictionnaire pour conserver une référence
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
gifdict = {}
Fenetre.mainloop()