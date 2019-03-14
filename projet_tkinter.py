from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import tkinter.messagebox
import tkinter.filedialog
import varCommunes as VC
import AlgoCSV

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

def drawGrid(event):
    for i in range(0, 1000, 1000//50):
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