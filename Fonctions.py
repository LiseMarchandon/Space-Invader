#-*- coding: utf-8 -*-
#Header
'''
Ce fichier a pour but de regrouper les fonctions générales du Jeu 
date de début : 04/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
#Importation nécessaire 
from tkinter.messagebox import askyesno

#Initialisation
L_missile = []
nbmissile = 0
canTouche = True
shot_rate = 500

#Fonctions du programme

def Clavier(event):
    '''
    La fonction gère les touches du clavier, et les déplacements qu'elles engendrent
    entrée : pression d'une touche (event)
    sorties : 
    '''
    from Missile import Missile #importation interne
    global posX, img_vaisseau, Canevas, Hauteur, Largeur, maFenetre, L_missile, nbmissile, spriteVaisseau, canTouche '''Récupération des données utiles'''

    touche = event.keysym
    if touche == "right" and posX + 50 < Largeur:
        posX += 20
    if touche == "left" and posX - 50 > 0:
        posX -= 20
    if touche == "space" and canTouche == True:


