from tkinter import Tk, Button, Label, StringVar, Frame, PhotoImage, Canvas

def LancerJeu():
    return 0

def MouvementJoueur(event):
    global PosX, PosY
    touche = event.keysym
    if touche == 'left':
        PosY -= 20
    if touche == 'rigth':
        PosY += 20
    Canevas.coords(joueur, PosY)