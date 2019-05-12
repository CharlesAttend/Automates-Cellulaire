# Automates-Cellulaires :

## Projet d'ISN 2019
  Génération d'un automate cellulaire pour simuler un feu de forêt.

Par Augustin Viard, Charles Vin et Benjamin Hubinet

## Quelques captures d'écrans du projet :

#### Propgation du feu sur une forêt de dimensions 50x50:

![propagation_feu_50_50png](https://user-images.githubusercontent.com/38909289/57470182-87255400-7288-11e9-8f63-5006eddd7f4b.png)

#### Propagation du feu sur un forêt de dimensions 10x10:

![propagation_feu_10_10png](https://user-images.githubusercontent.com/38909289/57470199-91475280-7288-11e9-958b-cf5e7f21c309.png)

## Informations complémentaires :

-Chaque cellule a une surface de 4m².
Cela fait que la génération 50x50 représente en réalité une surface de 1 hectare, la génération 10x10 représente en réalité une surface de 1/4 d'hectare.

-Lorsqu'une cellule de type arbre est en feu, l'algorithme va tester les 8 cellules adjacentes à celle-ci, si c'est un arbre et qu'une certaine probabilité est vérifiée (dans notre cas : 0.45, soit 45% de chance que le feu se propage), alors le feu se propage.

-Toutes les textures utilisées ont été réalisées par Augustin.
