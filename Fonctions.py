'''
ce fichier a pour but de regrouper les fonctions générales du jeu 
date de début: 04/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

from tkinter.messagebox import askyesno


liste_missile= []
nbmissile = 0
Touche = True
shot_rate = 500

''' Fonction qui gère les touches du clavier '''

def Clavier(event):
    from Missile import Missile 

    global posX, posY, img_vaisseau, Canevas, Hauteur, Largeur, maFenetre, liste_missile, nbmissile, spriteVaisseau, Touche

    touche = event.keysym
    if touche == "d" and posX + 50 < Largeur:
        posX += 20
    if touche == "q" and posX - 50 > 0:
        posX -= 20

    if touche == "space" and Touche == True : 
        m = Missile(posX, Hauteur - 50 - spriteVaisseau.heigh() / 2, nbmissile, -20, "imagemissile")
        nbmissile += 1
        liste_missile.append(m)
        m.afficherMissile()
        tir()

    Canevas.coords(image_vaisseau, posX, Hauteur - 30)

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
    global liste_missile, maFenetre
    if (vaisseau.isAlive()) :
        for i in range(len(liste_missile)):
            pX, pY = liste_missile[i].getPos()
            if (liste_missile[i.isAlive()]):
                pY += liste_missile[i].getSpeed()
                liste_missile[i].setPos(pX,pY)
                liste_missile[i].collisionEnnemy(vaisseau)
                liste_missile[i].collisionJoueur(vaisseau)
                liste_missile[i].collisionShield()
            else:
                Canevas.delete(liste_missile[i].gteImg())
    if (vaisseau.isAlive() and level.getVictoire() == False and level.getItsOver()== False):
        maFenetre.after(50, gestionMissile, vaisseau, level)
    
'''Fonction qui gère le jeu lorsque le joeur perd'''

def gameOver(vaisseau,level):
    global maFenetre, Canevas
    if (vaisseau.isAlive() == False):
        if askyesno("Game Over", "Replay?"):
            level.setupLevel(vaisseau)
        else:
            maFenetre.destroy()
    elif vaisseau.isAlive() == True and level.getisOver() == False and level.gteVictoire() == False:
        maFenetre.after(100, gameOver, vaisseau, level)

