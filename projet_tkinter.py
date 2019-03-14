from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import tkinter.messagebox
import tkinter.filedialog
import varCommunes as VC

def Clic(event):
    X = event.x
    Y = event.y
    X = int(X/100)*100
    Y = int(Y/100)*100
    vg.setCoordDepartFeu(X,Y)

def enregistrer():
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    image = ImageGrab.grab((x + 2, y + 2, x + w - 2, y + h - 2))
    image.save("Feu.png")

def dix () :
    vg.setLargeur(800)
    vg.setHauteur(800)
    vg.setNbCell(10)
    print(vg.getHauteur())
    print(vg.getLargeur())
    print(vg.getNbCellules())

def cinquante () :
    vg.setLargeur(800)
    vg.setHauteur(900)
    vg.setNbCell(50)
    

def cent () :
    vg.setLargeur(800)
    vg.setHauteur(800)
    vg.setNbCell(100)

def sim_auto():
    pass

def pasapas():
    pass

vg = VC.varGlobales()

Fenetre = Tk()
Fenetre.title("Image")
Fenetre.geometry('1000x1000')
canvas = Canvas(Fenetre, width = 800, height = 800, background='yellow')
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

# Affichage du menu
Fenetre.config(menu = menubar)


# Utilisation d'un dictionnaire pour conserver une référence
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
gifdict = {}
Fenetre.mainloop()
