'''
ce fichier a pour but de gérer les missiles du jeu
date de début: 07/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
import Fonctions
from tkinter import PhotoImage
import Niveau

class Missile:

    '''Initialisation d'un missile'''

    def __init__(self, posx, posy, num,speed, img):
        self.__name = num
        self.__posx = posx
        self.__posy = posy
        self.__isAlive = True
        self.__sprite = None
        self.__img = img
        self.__speed = speed
    
    '''Fonctions permettant de récupérer les attributs de l'objet'''

    def getImg(self):
        return self.__img
    
    def getPos(self):
        return self.__posx, self.__posy
    
    def getSpeed(self):
        return self.__speed
    
    '''Fonctions permettant de modifier les attributs de l'objet'''

    def setPos(self, x, y):
        self.__posx = x
        self.__posy = y
        Fonctions.Canevas.coords(self.__img, self.__posx, self.__posy)

    '''Affichage d'un missile'''

    def afficherMissile(self):
        self.__sprite = PhotoImage(file= self.__img)
        img_missile = Fonctions.Canevas.create_image(self.__posx, self.__y, image = self.__sprite)
        self.__img = img_missile
        Fonctions.Canevas.image = self.__sprite
    
    '''Vérification de l'existence du missile'''

    def isAlive(self):
        return self.__isAlive
    
    '''Collision avec un ennemie'''

    def collisionEnnemy(self, vaisseau):
        tab_ennemy = Niveau.tableau
        dX = Niveau.offsetX
        dY = Niveau.offsetY
        liste_ennemies = []
        for i in tab_ennemy:
            for j in tab_ennemy:
                if(type(j) != type(None)):
                    liste_ennemies.append(j)
                else:
                    liste_ennemies.append([])
        for ennemy in liste_ennemies:
            if(ennemy != []):
                Pos = ennemy.getPos()
                if Pos[0] - dX / 2 < self.__posx < Pos[0] + dX / 2 and Pos[1] - dY / 2 < self.__posy < Pos[1] +dY:
                    i, j = ennemy.getIdent()
                    Fonctions.Canevas.delete(tab_ennemy[i][j].getImg())
                    spriteMort =  PhotoImage(file = "sourismorte.png")
                    tab_ennemy[i][j].affichageEnnemyMort(spriteMort)
                    Fonctions.maFenetre.after(200, self.detruireEnnemy, tab_ennemy[i][j].getImgMort())
                    self.__isAlive = False
                    vaisseau.setScore(vaisseau.getScore() + tab_ennemy[i][j].getPoints())
                    Niveau.tableau[i][j] = None
    
    '''Collision avec un joueur'''

    def collisionJoueur(self, vaisseau):
        dX = Fonctions.spriteVaisseau.width()
        dY = Fonctions.spriteVaisseau.height()
        if Fonctions.posX - dX / 2 < self.__posx < Fonctions.posX - 30 + dX / 2 and Fonctions.Hauteur - 30 - dY / 2 < self.__posy < Fonctions.Hauteur - 30 + dY / 2:
            self.__isAlive = False 
            Fonctions.Canevas.delete(Niveau.tabCoeur[vaisseau.getVie() - 1])
            vaisseau.setVie(vaisseau.getVie() - 1)
            print(vaisseau.getVie())

    '''Collision avec un bouclier'''
    def collisionShield(self):
        b_shield = Niveau.L_rocher
        dX = 25
        dY = 25 
        liste_shield = []
        for i in b_shield:
            for j in i:
                if(type(j) != type(None)):
                    liste_shield.append(j)
                else:
                    liste_shield.append([])
        for shield in liste_shield:
            if (shield != []):
                Pos =  shield.getPos()
                if Pos[0] - dX / 2 < self.__posx < Pos[0] + dX / 2 and Pos[1] - dY / 2 < self.__posy < Pos[1] + dY:
                    i,j = shield.getIdent()
                    Fonctions.Canevas.delete(b_shield[i][j].getImg())
                    self.__isAlive =  False
                    Niveau.L_rocher[i][j] = None

    '''Détruit le missile'''
    
    def detruireEnnemy(self, img):
        Fonctions.Canevas.delete(img)




    
    