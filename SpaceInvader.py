'''
ce fichier a pour but d'être le fichier où on lance le code principal du jeu 
date de début: 05/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

from tkinter import Tk, PhotoImage, Canvas, Menu
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
Fonctions.Canevas = Canvas(Fonctions.maFenetre, width = Fonctions.Largeur, height = Fonctions.Hauteur)
spritebg = PhotoImage(file = "ciel.png")
image_bg = Fonctions.Canevas.create_image(Fonctions.Largeur / 2, Fonctions.Hauteur / 2, image = spritebg)
Fonctions.Canevas.image = spritebg
Fonctions.spriteVaisseau = PhotoImage(file = str(joueur.getImg()))
Fonctions.img_vaisseau = Fonctions.Canevas.create_image(Fonctions.posX, Fonctions.Hauteur - 30, image = Fonctions.spriteVaisseau)
Fonctions.Canevas.image = Fonctions.spriteVaisseau
Fonctions.Canevas.focus_set()


'''Menu du jeu'''
menubar = Menu(Fonctions.maFenetre)
menu1 = Menu(menubar, tearoff = 0)
vaisseau = joueur
menu1.add_command(label="Nouvelle Partie", command= lambda vaisseau : niveau.setupLevel(vaisseau))
vaisseau = joueur
menu1.add_separator()
menu1.add_command(label="Quitter", command = Fonctions.maFenetre.destroy)
menubar.add_cascade(label = "Jeu", menu = menu1)
menu2 = Menu(menubar, tearoff = 0)
menu2.add_command(label= "À propos")
menubar.add_cascade(label="Aide", menu=menu2)
Fonctions.maFenetre.config(menu=menubar)

'''Affichage des éléments'''
Fonctions.Canevas.pack(side="left",padx = 5, pady =5)
Fonctions.maFenetre.mainloop()