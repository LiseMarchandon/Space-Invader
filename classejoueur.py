
from tkinter import Tk, Button, Label, StringVar, Frame, PhotoImage, Canvas


class Joueur:
    def __init__(self,posX,posY):
        self.__x=posX
        self.__y=posY
    
    def RecupPositionX(self):
        return self.__x

    def RecupPositionY(self):
        return self.__y

    def MouvementJoueurL(self):
            self.__x -= 20
    
    def MouvementJoueurR(self):
            self.__x += 20