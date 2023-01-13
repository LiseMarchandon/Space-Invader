'''
ce fichier a pour but 
date de début: 08/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter import PhotoImage
import Fonctions

class Bouclier:
    """Initialisation d'un bouclier"""
    def __init__(self, img, posX, posY, ident):
        self._img = img
        self._posX = posX
        self._posY = posY
        self._ident = ident
        self._sprite = PhotoImage(file = str(self._img))
        
    """Fonctions permettant de recupérer les attributs de l'objet à l'extérieur"""
    def getPos(self):
        return [self._posX, self._posY]

    def getImg(self):
        return self._img

    def getTaille(self):
        return self._ligne, self._colonne

    def getSprite(self):
        return self._sprite
    
    def getIdent(self):
        ident = self._ident
        return int(ident[0]),int(ident[1:])
        
    """Fonctions permettant de modifier les attributs de l'objet à l'extérieur"""
    def setPos(self, x, y):
        self._posX = x
        self._posY = y
    
    """Affichage d'un bloc de bouclier"""
    def afficherBouclier(self, sprite):
        spriteShield = sprite
        img_shield = Fonctions.Canevas.create_image(self._posX ,self._posY , image = spriteShield)
        self._img = img_shield
        Fonctions.Canevas.image = spriteShield 