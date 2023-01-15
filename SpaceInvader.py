'''
ce fichier a pour but d'être le fichier où on lance le code principal du jeu 
date de début: 05/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: rajouter un autre menu pour la partie 'À Propos', cheat-codes, demande à l'utilisateur de renseigner son nom
version pyhton 3.7
'''

from tkinter import Tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Menu
from Vaisseau import Vaisseau
from Niveau import Niveau
import Fonctions

monVaisseau = Vaisseau("SpaceShip", 3, "chat2.png")
monNiveau = Niveau(2, 6)

"""Initialisation de la fenêtre"""
Fonctions.maFenetre = Tk()
Fonctions.Largeur = 800
Fonctions.Hauteur = 600
Fonctions.posX = Fonctions.Largeur / 2
Fonctions.maFenetre.title('Space Invader') 

"""Fenêtre du jeu"""
Fonctions.Canevas = Canvas(Fonctions.maFenetre, width = Fonctions.Largeur, height = Fonctions.Hauteur)
spritebg = PhotoImage(file = "ciel.png")
img_bg = Fonctions.Canevas.create_image(Fonctions.Largeur / 2, Fonctions.Hauteur / 2, image = spritebg)
Fonctions.Canevas.image = spritebg
Fonctions.spriteVaisseau = PhotoImage(file = str(monVaisseau.getImg()))
Fonctions.img_vaisseau= Fonctions.Canevas.create_image(Fonctions.posX, Fonctions.Hauteur - 30, image = Fonctions.spriteVaisseau)
Fonctions.Canevas.image = Fonctions.spriteVaisseau
Fonctions.Canevas.focus_set()

"""Menu du jeu"""
menubar = Menu(Fonctions.maFenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle partie", command = lambda vaisseau=monVaisseau:monNiveau.setupLevel(vaisseau)) #fonction lambda qui nous permet d'associer à l'élément vaisseau un niveau pour lancer le jeu
menu1.add_separator()
menu1.add_command(label="Quitter", command=Fonctions.maFenetre.destroy)
menubar.add_cascade(label="Jeu", menu=menu1)
Fonctions.maFenetre.config(menu=menubar)

"""Affichage des éléments"""
Fonctions.Canevas.pack(side="left", padx=5, pady=5)
Fonctions.maFenetre.mainloop()