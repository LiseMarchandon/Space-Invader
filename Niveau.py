'''
ce fichier a pour but de regrouper les Fonctions générales du jeu 
date de début: 08/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

from tkinter import PhotoImage
from tkinter import Label
from tkinter import StringVar
from tkinter.messagebox import askyesno

import Fonctions
from Ennemie import Ennemie
import random


class Niveau:
    """Initialisation de l'objet niveau"""
    def __init__(self, ligne, colonne):
        self._ligne = ligne
        self._colonne = colonne
        self._itsOver = False
        self._label_score = None
        self._victoire = False
        self._tab_Special = []
    
    
    """Fonctions permettant de recupérer les attributs de l'objet à l'extérieur"""
    def getItsOver(self):
        return self._itsOver

    def getVictoire(self):
        return self._victoire
    
    def setupLevel(self, vaisseau):
        """Initialise les paramètres d'un niveau"""
        self.resetLevel(vaisseau)
        Fonctions.Canevas.bind("<KeyPress>", Fonctions.Clavier)
        self.setupEnnemies(vaisseau)
        self.setupShield()
        self.attaqueEnnemy(vaisseau)
        self.setupHUD(vaisseau)
        self.specialEnnemy()
        self.victoire()
        self.finNiveau(vaisseau)
        Fonctions.gameOver(vaisseau, self)
        if(len(Fonctions.L_missile) != 0):
            Fonctions.gestionMissile(vaisseau, self)
   
    def setupEnnemies(self, vaisseau):
        """Gestion du tableau d'ennemies """
        from Ennemie import Ennemie
        global tableau, spriteEnnemy, compteurX, compteurY, deplacementDroite, offsetX, offsetY
        
        compteurX = 0
        deplacementDroite = True
        tableau = [[0 for i in range(self._ligne)] for i in range(self._colonne)]
        ennemyBase = Ennemie("test","souris2.png", 0, 0, 0, 25)
        spriteEnnemy = PhotoImage(file = str(ennemyBase.getImg()))
        offsetX = spriteEnnemy.width()
        offsetY = spriteEnnemy.height()
        separationX = 50
        separationY = 70
        for i in range(self._colonne):
            for j in range(self._ligne):
                posX = offsetX + separationX*i
                posY = offsetY + separationY*j
                ennemy = Ennemie('Alien'+str(i)+str(j), "souris2.png", str(i)+str(j), posX, posY, 25)
                ennemy.affichageEnnemy(spriteEnnemy)
                tableau[i][j] = ennemy
        self.deplacementEnnemies(vaisseau)
        
        
    def deplacementEnnemies(self, vaisseau):
        """Deplacement des ennemies"""
        global tableau, spriteEnnemy, compteurX, compteurY, deplacementDroite, offsetX, offsetY
        
        descente = False
        a = (Fonctions.Largeur/offsetX - self._colonne - 1)*5
        if(compteurX <= 0):
            deplacementDroite = True
            descente = True
        if(compteurX >= a):
            deplacementDroite = False
            descente = True
        if(deplacementDroite):
            compteurX += 1
            decalageX = offsetX / 5
        else:
            decalageX = -offsetX / 5
            compteurX -= 1
        if(vaisseau.isAlive()):
            for i in range(len(tableau)):
                for j in range(len(tableau[0])):
                    if(type(tableau[i][j]) != type(None)):
                        pX, pY = tableau[i][j].getPos()
                        if(descente):
                            pY += offsetY
                            tableau[i][j].setPos(pX, pY)
                        else:
                            tableau[i][j].setPos(pX + decalageX, pY)
        if(vaisseau.isAlive() and self._itsOver == False and self._victoire == False):           
            Fonctions.maFenetre.after(100, self.deplacementEnnemies, vaisseau)
        
    def attaqueEnnemy(self, vaisseau):
        """Tire aléatoire des ennemies"""
        if(vaisseau.isAlive()):
            tirage = random.randint(0, self._colonne - 1)
            for i in range(self._ligne):
                if(type(tableau[tirage][self._ligne - i - 1]) != type(None)):
                    tableau[tirage][self._ligne - i - 1].attaque()
                    break
        if(vaisseau.isAlive() and self._itsOver == False and self._victoire == False):    
            Fonctions.maFenetre.after(500, self.attaqueEnnemy, vaisseau)
            
    def resetLevel(self, vaisseau):
        """Reinitialisation du niveau en cas de victoire ou defaite"""
        vaisseau.setVie(3)
        for i in range(len(Fonctions.L_missile)):
            Fonctions.Canevas.delete(Fonctions.L_missile[i].getImg())
        Fonctions.L_missile.clear()
        self._victoire = False
        if type(self._label_score) != type(None):
            self._label_score.pack_forget()
            vaisseau.setScore(0)
        
    def setupShield(self):
        """Initialisation du tableau de bouclier"""
        from Bouclier import Bouclier
        global spriteShield, L_rocher, pattern_rocher
        
        b_standart = Bouclier("panier.png", 100, 100, 0)
        spriteShield=PhotoImage(file = str(b_standart.getImg()))
        L_rocher = []
        x = Fonctions.Largeur
        nb_slot = x / spriteShield.width()
        pattern = [0,1,1,1,0]
        pattern_rocher = [pattern for i in range(int(nb_slot / len(pattern)))]
        pat = []
        
        for i in pattern_rocher:
            for j in i:
                pat.append(j)
        L_rocher = [[None for i in range(len(pat))] for j in range(2)]
        for i in range(len(L_rocher)):
            for j in range(len(L_rocher[0])):
                if(pat[j] == 1):                
                    roc = Bouclier("panier.png", 25 + 25 * j, 450 + 25 * i, str(i) + str(j))
                    roc.afficherBouclier(spriteShield)
                    L_rocher[i][j] = roc
                    
    def setupHUD(self, vaisseau):
        """Initialise l'interface du jeu comme les points de vie"""
        global spriteCoeur, tabCoeur, label_score
        
        spriteCoeur = PhotoImage(file = 'vie.png')
        tabCoeur = []
        
        for i in range(vaisseau.getVie()):
            vaisseau.afficherVie(spriteCoeur,800 - 30 * (i + 1), 30)
        sc = StringVar()
        self._label_score = Label(Fonctions.Canevas, bg="white", textvariable = sc)
        self.affichageScore(vaisseau, sc)
        self._label_score.place(x = 5, y = 5, width = 100, height = 50)
    
    
    def affichageScore(self, vaisseau, sc):
        """Affiche le score"""
        sc.set("Score : " + str(vaisseau.getScore()))
        Fonctions.maFenetre.after(200, self.affichageScore, vaisseau, sc)
        
    def victoire(self):
        """Test si on a un cas de victoire"""
        global tableau
        self._victoire = True
        for i in range(len(tableau)):
            for j in range(len(tableau[0])):
                if type(tableau[i][j]) != type(None):
                    self._victoire = False
        Fonctions.maFenetre.after(100, self.victoire)
    
    def finNiveau(self, vaisseau):
        """Apparition d'une fenêtre en cas de victorie"""
        if self.getVictoire() == True:
            if askyesno("Victoire", "Voulez-vous rejouer ?"):
                self.setupLevel(vaisseau)
            else:
                Fonctions.maFenetre.destroy()
        elif self.getVictoire() == False and vaisseau.isAlive() == True and self.getItsOver() == False:
            Fonctions.maFenetre.after(100, self.finNiveau, vaisseau)

    def specialEnnemy(self):
        """Apparition d'un ennemie special"""
        global spriteSpecial
        special = Ennemie('Special', "sourisboss.png", 82, 100, 40, 150)
        spriteSpecial = PhotoImage(file = str(special.getImg()))
        special.affichageEnnemy(spriteSpecial)
        self._tab_Special.append(special)
        Fonctions.maFenetre.after(100, self.depSpecial, special, spriteSpecial, True, 0)
        
    def depSpecial(self, special, sprite, direction, compteur):
        """Gere le deplacement de l'ennemie special et le fait apparaitre quelques secondes"""
        pX, pY = special.getPos()
        versDroite = direction
        if pX + sprite.width()/2 > Fonctions.Largeur and versDroite == True:
            versDroite = False
        elif pX - sprite.width() / 2 < 0 and versDroite == False:
            versDroite = True
        if(versDroite):
            pX += 10
        else:
            pX -= 10
        compteur += 1
        special.setPos(pX, pY)
        if(compteur >= 240):
            Fonctions.Canevas.delete(str(special.getImg()))
        Fonctions.maFenetre.after(50, self.depSpecial, special, sprite, versDroite, compteur)