# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import tkinter.messagebox
import tkinter.filedialog
import AlgoCSV
import loadAlgo
import varCommunes as VC
import algorithmeForet as algoForet

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
    vg.setLargeur(800)
    vg.setHauteur(800)
    vg.setNbCell(10)

def cinquante () :
    a = varCommunes.varGlobales(900, 800, 50)

def cent () :
    a = varCommunes.varGlobales(800, 800, 100)

def sim_auto():
	tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), loadAlgoForet.getCellEnFeu(), loadAlgoForet.getListeForet()) #On test d'abord si le feu peut se propager
																																			#sur les 8 cases autour de l'arbre
	loadAlgoForet.setNewListeForet(tmpListeForet)							#On actualise la liste de la foret
	for i in range(loadAlgoForet.getCellUpdated(),len(tmpCellEnFeu), 2):	#On créer une boucle permettant d'ajouter à la liste des cellules en feu les coordonnées des prochains arbre à brûler
		loadAlgoForet.augmentCellEnFeu(tmpCellEnFeu[i], tmpCellEnFeu[i+1])

	for i in range(loadAlgoForet.getCellUpdated(), len(tmpCellEnFeu), 2): #On affiche les nouveaux arbres à prendre feu...
		pass 	#...

	loadAlgoForet.augmentCellUpdated(2)
    Fenetre.update()				#On raffraîchit l'écran
    canvas.after(2000, sim_auto)	#On appelle de nouveau la fonction de simulation après 2 secondes

def pasapas():
    tmpCellEnFeu, tmpListeForet = algoForet.propagationFeu(vg.getNbCellules(), loadAlgoForet.getCellEnFeu(), loadAlgoForet.getListeForet()) #On test d'abord si le feu peut se propager
																																			#sur les 8 cases autour de l'arbre
	loadAlgoForet.setNewListeForet(tmpListeForet)							#On actualise la liste de la foret
	for i in range(loadAlgoForet.getCellUpdated(),len(tmpCellEnFeu), 2):	#On créer une boucle permettant d'ajouter à la liste des cellules en feu les coordonnées des prochains arbre à brûler
		loadAlgoForet.augmentCellEnFeu(tmpCellEnFeu[i], tmpCellEnFeu[i+1])

	for i in range(loadAlgoForet.getCellUpdated(), len(tmpCellEnFeu), 2): #On affiche les nouveaux arbres à prendre feu...
		pass 	#...

	loadAlgoForet.augmentCellUpdated(2)
    Fenetre.update()				#On raffraîchit l'écran

def drawGrid(event):
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
                canvas.create_image(cordX, cordY, anchor=tkinter.NW, image=grass )



vg = VC.varGlobales()

# Génère ton CSV ici.
loadAlgoForet = loadAlgo.loadAlgo()
loadAlgoForet.setListeForet()

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