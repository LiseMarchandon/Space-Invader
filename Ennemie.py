'''
ce fichier a pour but de gérer les ennemis
date de début: 07/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter import PhotoImage
import Fonctions

class Ennemie:

    def __init__(self, nom, img, ident, x, y, points):

        '''
        cette méthode initialise l'objet ennemie
        entrées: l'objet visé, nom, l'image, l'identifiant (même explication que pour les boucliers), position selon x et selon y, les points apportés par chaque ennemie
        sorties: pas de sortie
        '''

        self._nom = nom
        self._img = img
        self._imgMort = None
        self._ident = ident
        self._x = x
        self._y = y
        self._points = points
        self._sprite = PhotoImage(file = str(self._img))
    

    def getPoints(self):

        '''
        cette méthode permet de récupérer les points de l'ennemie
        entrées: l'objet visé
        sorties: nombre de points (entier)
        '''

        return self._points
    
    def getImg(self):

        '''
        cette méthode permet de récupérer l'image de l'ennemie
        entrées: l'objet visé
        sorties: image (str)
        '''

        return self._img
    
    def getImgMort(self):

        '''
        cette méthode permet de récupérer l'image de l'ennemie lorsqu'il est mort
        entrées: l'objet visé
        sorties: image (str)
        '''

        return self._imgMort
    
    def getIdent(self):

        '''
        cette méthode permet de récupérer l'identifiant assoscié à chaque ennemie
        entrées: l'objet visé
        sorties: identifiant du premier ennemie sous forme d'un entier et les identifiants des ennemies suivants sous forme d'entiers
        '''

        ident = self._ident
        return int(ident[0]),int(ident[1:])
    
    def getPos(self):

        '''
        cette méthode permet de récupérer la position des ennemies
        entrées: l'objet visé
        sorties: position selon x et y sous forme d'une liste
        '''

        return [self._x, self._y]
    
    def getSprite(self):

        '''
        cette méthode permet de récupérer l'image de l'ennemie mais contrairement à getImg, ici elle est prête à intéragir avec l'interface tkinter
        entrées: l'objet visé
        sorties: nombre de points (entier)
        '''

        return self._sprite
    
    
    def setIdent(self, ident):
        """
        Fonction permettant de modifier l'identifiant de l'ennemie
        entrées: objet ennemie, identifiant
        sorties: pas de sortie
        """
        self._ident = ident
    
    def setPos(self, x, y):
        """
        Fonction permettant de modifier la position de l'ennemie
        entrées: objet ennemie, position selon x, position selon y
        sorties: pas de sortie
        """
        self._x = x
        self._y = y
        Fonctions.Canevas.coords(self._img, self._x, self._y)
    
    
    def affichageEnnemy(self, sprite):
        """
        fonction qui affiche l'ennemie vivant
        entrées: objet ennemie, représentation
        sorties: pas de sortie
        """
        spriteEnnemy = sprite
        img_ennemy = Fonctions.Canevas.create_image(self._x ,self._y , image = spriteEnnemy)
        self._img = img_ennemy
        Fonctions.Canevas.image = spriteEnnemy  
    
    def affichageEnnemyMort(self, sprite):
        
        """
        fonction qui affiche l'ennemie mort
        entrées: objet ennemie, représentation
        sorties: pas de sortie
        """
        spritMort = sprite
        img_mort = Fonctions.Canevas.create_image(self._x, self._y, image = spritMort)
        self._imgMort = img_mort
        Fonctions.Canevas.image = spritMort

    def attaque(self):
        """
        fonction qui permet de lancer un missile ennemi
        entrées: objet ennemie
        sorties: pas de sortie
        """
        from Missile import Missile
        self._missile = Missile(self._x, self._y + 70, Fonctions.nbmissile, 20, "missilesouris.png")
        Fonctions.nbmissile += 1
        Fonctions.L_missile.append(self._missile)
        self._missile.afficherMissile()
        

