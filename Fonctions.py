'''
ce fichier a pour but de regrouper les Fonctions générales du jeu 
date de début: 04/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter.messagebox import askyesno

"""Initialisation"""
L_missile=[]
nbmissile = 0
canTouche = True
shot_rate = 500


def Clavier(event):

    '''
    cette fonction gère les touches du clvier
    Importation à l'intérieur car probleme du cycle d'importation (vue sur internet) 
    '''

    from Missile import Missile 
    
    global posX, img_vaisseau, Canevas, Hauteur, Largeur, maFenetre, L_missile, nbmissile, spriteVaisseau, canTouche
    
    touche = event.keysym
    if touche == "d" and posX + 50 < Largeur:
        posX += 20
    if touche == "q" and posX - 50 > 0:
        posX -= 20
        
    if touche == "space" and canTouche == True:
            m=Missile(posX, Hauteur - 50 - spriteVaisseau.height() / 2, nbmissile, -20, "missile2.png")
            nbmissile+=1
            L_missile.append(m)
            m.afficherMissile()
            tir()
            
    Canevas.coords(img_vaisseau, posX, Hauteur-30)
    
def tir():

    '''
    cette fonction permet de limiter la cadence de tir
    '''

    global canTouche, maFenetre

    canTouche = False
    maFenetre.after(shot_rate, shoot)
    
def shoot():
    
    '''
    cette fonction permet de limiter la cadence de tir
    '''
    
    global canTouche
    canTouche = True
    
def gestionMissile(vaisseau, level):

    '''
    cette fonction gère les missiles, les collisions et le deplacement de ceux ci
    '''

    global L_missile, maFenetre

    if(vaisseau.isAlive()):
        for i in range(len(L_missile)):
            pX, pY = L_missile[i].getPos()
            if(L_missile[i].isAlive()):
                pY += L_missile[i].getSpeed()
                L_missile[i].setPos(pX, pY)
                L_missile[i].collisionEnnemy(vaisseau)
                L_missile[i].collisionJoueur(vaisseau)
                L_missile[i].collisionShield()
            else:
                Canevas.delete(L_missile[i].getImg())
    if(vaisseau.isAlive() and level.getVictoire() == False and level.getItsOver() == False):         
        maFenetre.after(50, gestionMissile, vaisseau, level)
    
    
def gameOver(vaisseau, level):

    '''
    cette fonction gère le jeu en cas de défaite
    '''

    global maFenetre, Canevas
    if(vaisseau.isAlive() == False):
        if askyesno("Défaite", "Voulez-vous rejouer ?"):
            level.setupLevel(vaisseau)
        else:
            maFenetre.destroy()
    elif vaisseau.isAlive() == True and level.getItsOver() == False and level.getVictoire() == False:
        maFenetre.after(100, gameOver, vaisseau, level)