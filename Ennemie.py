'''
ce fichier a pour but de gérer les 
date de début: 07/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter import PhotoImage
import Fonctions

class Ennemie:
    """Initialisation de l'objet ennemie"""
    def __init__(self, nom, img, ident, x, y, points):
        self._nom = nom
        self._img = img
        self._imgMort = None
        self._ident = ident
        self._x = x
        self._y = y
        self._points = points
        self._sprite = PhotoImage(file = str(self._img))
    
    """Fonctions permettant de recupérer les attributs de l'objet à l'extérieur"""
    def getPoints(self):
        return self._points
    
    def getImg(self):
        return self._img
    
    def getImgMort(self):
        return self._imgMort
    
    def getIdent(self):
        ident = self._ident
        return int(ident[0]),int(ident[1:])
    
    def getPos(self):
        return [self._x, self._y]
    
    def getSprite(self):
        return self._sprite
    
    """Fonctions permettant de modifier les attributs de l'objet à l'extérieur"""
    def setIdent(self, ident):
        self._ident = ident
    
    def setPos(self, x, y):
        self._x = x
        self._y = y
        Fonctions.Canevas.coords(self._img, self._x, self._y)
    
    
    def affichageEnnemy(self, sprite):
        """Affichage de l'ennemie vivant"""
        spriteEnnemy = sprite
        img_ennemy = Fonctions.Canevas.create_image(self._x ,self._y , image = spriteEnnemy)
        self._img = img_ennemy
        Fonctions.Canevas.image = spriteEnnemy  
    
    def affichageEnnemyMort(self, sprite):
        """Affichage de l'ennemie mort"""
        spritMort = sprite
        img_mort = Fonctions.Canevas.create_image(self._x, self._y, image = spritMort)
        self._imgMort = img_mort
        Fonctions.Canevas.image = spritMort

    def attaque(self):
        """Lance un missile ennemie"""
        from Missile import Missile
        self._missile = Missile(self._x, self._y + 70, Fonctions.nbmissile, 20, "missilesouris.png")
        Fonctions.nbmissile += 1
        Fonctions.L_missile.append(self._missile)
        self._missile.afficherMissile()
        

