# -*- coding :utf-8 -*-
from PIL import Image
# Ouverture d'un fichier au format pgm binaire
ImageSource = Image.open("Mushroom2.png")
largeur,hauteur = ImageSource.size
ImageCible=Image.new("RGB",(largeur,hauteur))
for y in range(hauteur) :
    for x in range(largeur) :
        p=ImageSource.getpixel((x,y))
        q=(255-p[0],255-p[1],255-p[2])
        ImageCible.putpixel((x,y),q)
ImageCible.save("Mushroom2modif.png")
ImageCible.show()