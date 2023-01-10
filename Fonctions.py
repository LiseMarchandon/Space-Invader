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
    
    from Missile import Missile #importation à l'intérieur car problème du cycle

    global posX, img_vaisseau, Canevas, Hauteur, Largeur, maFenetre, L_missile, nbmissile, spriteVaisseau, canTouche #Récupération des données utiles

    touche = event.keysym
    if touche == "right" and posX + 50 < Largeur:
        posX += 20
    if touche == "left" and posX - 50 > 0:
        posX -= 20
    if touche == "space" and canTouche == True:
        m = Missile(posX, Hauteur - 50 - spriteVaisseau.height() / 2, nbmissile, -20, "missile2.png")
        nbmissile += 1
        L_missile.append(m)
        m.afficherMissile()
        tir()

    Canevas.coords(img_vaisseau, posX, Hauteur - 30)

'''Fonctions qui permettent de limiter la cadence des tirs'''

def tir():

    global Touche, maFenetre

    Touche =  False
    maFenetre.after(shot_rate, shoot)

def shoot():

    global Touche

    Touche = True

'''Fonction qui gère les missiles, les collisions et le deplacement de ces derniers'''

def gestionMissile(vaisseau, level):

    global L_missile, maFenetre

    if (vaisseau.isAlive()) :
        for i in range(len(L_missile)):
            pX, pY = L_missile[i].getPos()
            if (L_missile[i].isAlive()):
                pY += L_missile[i].getSpeed()
                L_missile[i].setPos(pX,pY)
                L_missile[i].collisionEnnemy(vaisseau)
                L_missile[i].collisionJoueur(vaisseau)
                L_missile[i].collisionShield()
            else:
                Canevas.delete(L_missile[i].getImg())
    if (vaisseau.isAlive() and level.getVictoire() == False and level.getItsOver()== False):
        maFenetre.after(50, gestionMissile, vaisseau, level)
    
'''Fonction qui gère le jeu lorsque le joueur perd'''

def gameOver(vaisseau,level):

    global maFenetre, Canevas

    if (vaisseau.isAlive() == False):
        if askyesno("Game Over", "Voulez-vous rejouer?"):
            level.setupLevel(vaisseau)
        else:
            maFenetre.destroy()
    elif vaisseau.isAlive() == True and level.getisOver() == False and level.gteVictoire() == False:
        maFenetre.after(100, gameOver, vaisseau, level)

