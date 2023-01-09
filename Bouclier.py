'''
ce fichier a pour but 
date de début: 08/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

from tkinter import PhotoImage
import Fonctions

class Bouclier:

    '''Initialisation d'un bouclier'''

    def __init__(self, img, posX, posY, id):
        self.__img = img
        self.__posX = posX
        self.__posY = posY
        self.__id = id
        self.__sprite = PhotoImage(file = str(self.__img))
    
    '''Fonctions permmettant de récuperer les attributs de l'objet'''

    def getPos(self):
        return [self.__posX, self.__posY]
    
    def getImg(self):
        return self.__img
    
    def getTaille(self):
        return self.__ligne, self.__colonne
    
    def getSprite(self):
        return self.__sprite 
    
    def getIdent(self):
        id = self.__id
        return int(id[0], int(id[1:]))
    
    '''Fonction permettant de modifier les attributs de l'objet'''

    def setPos(self, x, y):
        self.__x = x
        self.__y = y
    
    '''Affichage d'un bloc de bouclier'''

    def affichageBouclier(self, sprite):
        spriteShield = sprite
        img_shield = Fonctions.Canevas.create_image(self.__posX, self.__posY, image = spriteShield)
        self.__img = img_shield
        Fonctions.Canevas.image = spriteShield 
    
    