'''
ce fichier a pour but d'être le fichier où on lance le code principal du jeu 
date de début: 05/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

from tkinter import Tk, Button, Label, StringVar, Frame, PhotoImage, Canvas, Menu
from Joueur import Joueur
from Niveau import Niveau
import Fonctions

joueur = Joueur("Chat", 3, "chat2.png")
niveau = Niveau(2,6)

'''Initialisation de la fenêtre'''
Fonctions.maFenetre = Tk()
Fonctions.Largeur = 800
Fonctions.Hauteur = 600
Fonctions.posX = Fonctions.Largeur /2

'''Fenêtre du jeu'''
Fonctions.Canevas = Canvas(Fonctions.maFenetre, width = Fonctions.largeur, heightf= Fonctions.Hauteur)
spritebg = PhotoImage(file = "ciel.png")
image_bg = Fonctions.Canevas.create_image(Fonctions.Largeur / 2, Fonctions.Hauteur / 2, ilage = spritebg)
Fonctions.Canevas.image =spritebg
Fonctions.spriteVaisseau = PhotoImage(file = str(joueur.getImg()))
Fonctions.img_vaisseau = Fonctions.Canevas.create_image(Fonctions.posX, Fonctions.Hauteur - 30, image = Fonctions.spriteVaisseau)
Fonctions.Canevas.image = Fonctions.spriteVaisseau
Fonctions.Canevas.focus_set()


'''Menu du jeu'''
menubar = Menu(Fonctions.maFenetre)
menu1 = Menu(menubar,tearoff = 0)
menu1.add_command(label="New Game", command= Fonctions.maFenetre.destroy)
vaisseau = joueur
niveau.setupLevel(vaisseau)
menu1.add__separator()
menu1.add__command(label="Exit", command = Fonctions.maFenetre.destroy)
menubar.add__cascade(label = "Game", menu = menu1)
menu2 = Menu(menubar, tearoff = 0)
menu2.add__command(label= "About")
menubar.add__cascade(label="Help", menu=menu2)
Fonctions.maFenetre.config(menu=menubar)

'''Affichage des éléments'''
Fonctions.Canevas.pack(side="left",padx = 5, pady =5)
Fonctions.maFenetre.mainloop()