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
    """Initialisation d'un missile"""
    def __init__(self,pos_x,pos_y,num, speed, img):
        """Cette méhode initialise l'objet missile
            entrées: position ordonnée et abscisse, nom, vitesse de déplacement et image associée
            sorties: pas de sortie"""

        self.name = num
        self.pos_x = pos_x
        self.pos_y = pos_y
        self._isAlive = True
        self.sprite = None
        self.img = img
        self._speed = speed
    
    """Fonctions permettant de recupérer les attributs de l'objet à l'extérieur"""
    def getImg(self):
         """
        cette méthode récupère l'image du missile
        entrées: l'objet missile
        sorties: image du missile (dans notre cas c'est un chat)
        """
        return self.img
    
    def getPos(self):
         """
        cette méthode récupère la position du missile
        entrées: l'objet missile
        sorties: position selon x et position selon y
        """
        return self.pos_x, self.pos_y
    
    def getSpeed(self):
        """
        cette méthode récupère la vitesse du missile
        entrées: l'objet missile
        sorties: vitesse du missile
        """
        return self._speed
    
    
    def setPos(self, x, y):
        """
        Fonctions permettant de modifier les attributs de l'objet à l'extérieur
        entrées: coordonnées x et y et l'objet
        sorties: pas de sortie
        """
        self.pos_x = x
        self.pos_y = y
        Fonctions.Canevas.coords(self.img, self.pos_x, self.pos_y)
    
    
    def afficherMissile(self):
        """
        fonction qui affiche un missile
        entrée: objet missile
        sorties: pas de sorties
        """
        self.sprite=PhotoImage(file = self.img)    
        img_missile=Fonctions.Canevas.create_image(self.pos_x,self.pos_y,image = self.sprite)
        self.img=img_missile
        Fonctions.Canevas.image=self.sprite
    
    
    def isAlive(self):
        """
        fonction qui regarde si le missile est en vie
        entrée: objet missile
        sorties: True si le missile est vivant
        """
        return self._isAlive
    
    
    def collisionEnnemy(self, vaisseau):
        """
        fonction codant la collision avec un ennemie
        entrées: objet missile et objet vaisseau
        sorties : pas de sortie
        """
        tab_ennemy = Niveau.tableau
        dX = Niveau.offsetX
        dY = Niveau.offsetY
        L_pos_ennemies = []
        for i in tab_ennemy:
            for j in i:
                if(type(j) != type(None)):
                    L_pos_ennemies.append(j)
                else:
                    L_pos_ennemies.append([])
        for ennemy in L_pos_ennemies:
            if (ennemy != []):
                Pos = ennemy.getPos()
                if Pos[0] - dX / 2 < self.pos_x<Pos[0] + dX / 2 and Pos[1] - dY / 2 < self.pos_y<Pos[1] + dY:
                    i,j = ennemy.getIdent()
                    Fonctions.Canevas.delete(tab_ennemy[i][j].getImg())
                    spriteMort = PhotoImage(file = "sourismorte.png")
                    tab_ennemy[i][j].affichageEnnemyMort(spriteMort)
                    Fonctions.maFenetre.after(200, self.detruireEnnemy, tab_ennemy[i][j].getImgMort())
                    self._isAlive = False
                    vaisseau.setScore(vaisseau.getScore() + tab_ennemy[i][j].getPoints())
                    Niveau.tableau[i][j] = None
        
    
    def collisionJoueur(self, vaisseau):
        """
        fonction codant la collision avec un joueur
        entrées: objet missile, objet vaisseau
        sorties: pas de sortie 
        """
        dX = Fonctions.spriteVaisseau.width() 
        dY = Fonctions.spriteVaisseau.height() 
        if Fonctions.posX - dX / 2 < self.pos_x < Fonctions.posX + dX / 2 and Fonctions.Hauteur - 30 - dY / 2 < self.pos_y < Fonctions.Hauteur - 30 + dY / 2:
            self._isAlive = False
            Fonctions.Canevas.delete(Niveau.tabCoeur[vaisseau.getVie() - 1])
            vaisseau.setVie(vaisseau.getVie() - 1)
            print(vaisseau.getVie())
            
    
    def collisionShield(self):
        """
        Fonction codant la collision avec un bouclier
        entrées: objet missile
        sorties: pas de sortie
        """
        b_shield = Niveau.L_rocher
        dX = 25 
        dY = 25
        L_pos_shield = []
        for i in b_shield:
            for j in i:
                if(type(j) != type(None)):
                    L_pos_shield.append(j)
                else:
                    L_pos_shield.append([])
        for shield in L_pos_shield:
            if (shield != []):
                Pos=shield.getPos()
                if Pos[0] - dX / 2 < self.pos_x < Pos[0] + dX / 2 and Pos[1] - dY / 2 < self.pos_y < Pos[1] + dY:
                    i,j = shield.getIdent()
                    Fonctions.Canevas.delete(b_shield[i][j].getImg())
                    self._isAlive = False
                    Niveau.L_rocher[i][j]=None
                    
        
    def detruireEnnemy(self, img):
        """
        fonction qui détruit le missile dans le canevas 
        entrées: objet missile et son image associée
        sorties: pas de sortie
        """
        Fonctions.Canevas.delete(img)