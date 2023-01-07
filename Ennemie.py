'''
ce fichier a pour but de gérer les 
date de début: 07/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

from tkinter import PhotoImage
import Fonctions

class Ennemie:
    '''Initialisation de l'objet ennemie'''
    def __init__(self, nom, image,id, x, y, points):
        self.__nom = nom
        self.__img = image
        self.__imgMort = None
        self.__id= id
        self.__x = x
        self.__y = y 
        self.__points = points
        self.__sprite =  PhotoImage(file = str(self.__img))
    
    '''Fonctions permettant de récupérer les attributs de l'obejt'''
    def getPoints(self):
        return self.__points
    
    def getImg(self):
        return self.__img
    
    def getImgMort(self):
        return self.__imgMort
    
    def getIdent(self):
        id = self.__id
        return int(id[0], int(id[1:]))
    
    def getPos(self):
        return self.__sprite
    
    '''Fonctions permettant de modifier les attributs de l'objet'''

    def setIdent(self):
        self.__id = id
    
    def setPos(self,x,y):
        self.__x = x
        self.__y = y
        Fonctions.Canevas.coordss(self.__img, self.__x, self.__y)

    def affichageEnnemy(self, sprite):
        '''Affichage de l'ennemie vivant'''
        spriteEnnemy = sprite
        img_ennemy = Fonctions.Canevas.create_image(self.__x, self.__y, image = spriteEnnemy)
        self.__img = img_ennemy 
        Fonctions.Canevas.image = spriteEnnemy

    def affichageEnnemyMort(self, sprite):
        '''Affiche de l'ennemi quand celui-ci est mort'''
        spriteMort = sprite
        img_mort = Fonctions.Canevas.create_image(self.__x, self.__y, image = spriteMort)
        self.__imgMort = img_mort
        Fonctions.Canevas.image = spriteMort
    
    def attaque(self):
        '''Lance un missile ennemie'''
        from Missile import Missile
        self.__missile = Missile(self.__x, self.__y +70, Fonctions.nbmissile, 20, "Image missile")
        Fonctions.nbmissile += 1
        Fonctions.liste_missile.append(self.__missile)
        self.__missile.afficherMissile()

