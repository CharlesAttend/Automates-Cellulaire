from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import tkinter.messagebox
import tkinter.filedialog
import varCommunes



def enregistrer():
    x = Canevas.winfo_rootx()
    y = Canevas.winfo_rooty()
    w = Canevas.winfo_width()
    h = Canevas.winfo_height()
    image=ImageGrab.grab((x+2, y+2, x+w-2, y+h-2))
    image.save("Feu.png")

def dix () :
    a = varCommunes.varGlobales(900, 900, 10)

def cinquante () :
    a = varCommunes.varGlobales(900, 900, 50)

def cent () :
    a = varCommunes.varGlobales(900, 900, 100)

def sim_auto():
    pass

def pasapas():
    pass

Fenetre = Tk()
Fenetre.title("Image")
Fenetre.geometry('1000x1000')
canvas = Canvas(Fenetre, width=900, height=900, background='yellow')
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
auto.grid(row = 0, column=0, sticky = "n")
manuel.grid(row = 1, column = 0, sticky = "n")

# Affichage du menu
Fenetre.config(menu=menubar)


# Utilisation d'un dictionnaire pour conserver une référence
canvas.grid(sticky = "s")
gifdict={}
Fenetre.mainloop()
