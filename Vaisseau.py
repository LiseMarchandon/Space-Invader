'''
ce fichier a pour but de regrouper les Fonctions générales du jeu 
date de début: 05/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

import Fonctions
import Niveau

'''Objet joueur'''
class Vaisseaus:

    '''Initialisation du joueur'''

    def __init__(self,nom,vie,photo):
        self.__vie = vie 
        self.__nom = nom        
        self.__image = photo
        self.__coeur = None
        self.__score = 0
    
    '''Fonctions permettant de récupérer les attrbuts de l'objet'''

    def getImg(self):
        return self.__image
    
    def getScore(self):
        return self.__score
    
    def getVie(self):
        return self.__vie
    
    "Fonctions permettant de modifier les attributs de l'objet"

    def setScore(self, score):
        self.__score = score
    
    def setVie(self, vie):
        self.__vie = vie
    
    '''Fonction qui détermine si le joueur est encore en vie'''

    def isAlive(self):
        return self.__vie != 0
    
    '''Fonction qui permet l'affichage d'un coeur de vie'''
    
    def afficherVie(self,sprite, posX, posY):
        spriteCoeur = sprite
        image_Coeur = Fonctions.Canevas.create_image(posX, posY, image = spriteCoeur)
        self.__coeur = image_Coeur
        Fonctions.Canevas.image = spriteCoeur
        Niveau.tabCoeur.append(image_Coeur)


