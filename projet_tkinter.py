from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import tkinter.messagebox
import tkinter.filedialog



def enregistrer():
    x = Canevas.winfo_rootx()
    y = Canevas.winfo_rooty()
    w = Canevas.winfo_width()
    h = Canevas.winfo_height()
    image=ImageGrab.grab((x+2, y+2, x+w-2, y+h-2))
    image.save("Feu.png")

def sim_auto():
    pass

def pasapas():
    pass

Fenetre = Tk()
Fenetre.title("Image")
Fenetre.geometry('1280x720')
canvas = Canvas(Fenetre, width=1280, height=700, background='yellow')

menubar = Menu(Fenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Enregistrer l'image",command=enregistrer)
menufichier.add_command(label="Quitter",command=Fenetre.destroy)
menubar.add_cascade(label="Feu", menu=menufichier)

auto = Button(Fenetre, text = "Simulation Automatique", bg = "green", command = sim_auto)
manuel = Button(Fenetre, text = "Simulation Pas à Pas", bg = "blue", command = pasapas)
auto.grid(row = 0, column=0, sticky = "n")
manuel.grid(row = 0, column = 1, sticky = "n")


# Affichage du menu
Fenetre.config(menu=menubar)


# Utilisation d'un dictionnaire pour conserver une référence
canvas.grid(row = 1, column=0, columnspan=2)
gifdict={}
Fenetre.mainloop()
