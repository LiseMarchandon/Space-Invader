'''
ce fichier a pour but de regrouper les Fonctions générales du jeu 
date de début: 08/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter import PhotoImage, Label, StringVar
from tkinter.messagebox import askyesno
import Fonctions 
from Ennemie import Ennemie
import random

class Niveau:
    '''Initialisation de l'objet niveau'''
    def __init__(self, ligne, colonne):
        self.__ligne = ligne
        self.__colonne = colonne
        self.__itsOver = False
        self.__labelScore = None
        self.__victoire = False
    
    '''Fonctions permettant de récupérer les attributs de l'objet'''
    def getItsOver(self):
        return self.__itsOver
    
    def getVictoire(self):
        return self.__victoire
    
    def setupLevel(self, vaisseau):
        '''Initialise les paramètres du niveau'''
        self.resetLevel(vaisseau)
        Fonctions.Canevas.bind("<KeyPress>", Fonctions.Clavier)
        self.setupEnnemies(vaisseau)
        self.setupShield()
        self.attaqueEnemy(vaisseau)
        #self.setupHUD(vaisseau)
        #self.specialEnnemy()
        self.victoire()
        self.finNiveau(vaisseau)
        Fonctions.gameOver(vaisseau, self)
        if (len(Fonctions.liste_missile)!= 0):
            Fonctions.gestionMissile(vaisseau, self)
    
    def setupEnnemies(self, vaisseau):
        '''Gestion du tableau d'ennemies'''
        from Ennemie import Ennemie
        global tableau, spriteEnnemy, compteurX, compteurY, deplacementDroite, offsetX, offsetY
        compteurX = 0 
        deplacementDroite = True 
        tableau = [[0 for i in range(self.__ligne)]for i in range(self.__colonne)] 
        ennemyBase = Ennemie("test","souris2.png", 0, 0, 0, 25)
        spriteEnnemy = PhotoImage(file= str(ennemyBase.getImg()))
        offsetX = spriteEnnemy.width()
        offsetY = spriteEnnemy.height()
        separationX = 50
        separationY = 70
        for i in range(self.__colonne):
            for j in range(self.__ligne):
                posX = offsetX + separationX*i
                posY = offsetY + separationY*j
                ennemy = Ennemie("Alien"+ str(i)+str(j), "souris2.png", str(i)+str(j), posX, posY, 25)
                ennemy.affichageEnnemy(spriteEnnemy)
                tableau[i][j] = ennemy
        self.deplacementEnnemies(vaisseau)
    
    def deplacementEnnemies(self, vaisseau):
        '''Fonction qui gère le déplacement des ennemies'''
        global tableau, spriteEnnemy, compteurX, compteurY, deplacementDroite, offsetX, offsetY
        descente = False
        a = (Fonctions.Largeur / offsetX - self.__colonne - 1) * 5
        if(compteurX <= 0):
            deplacementDroite = True
            descente = True
        elif(compteurX >= a):
            deplacementDroite = False
            descente = True
        elif (deplacementDroite):
            compteurX += 1
            decalageX = offsetX / 5
        else:
            decalageX = -offsetX / 5
            compteurX -= 1 
        if (vaisseau.isAlive()):
            for i in range(len(tableau)):
                for j in range(len(tableau[0])):
                    if(type(tableau[i][j]) != type(None)):
                        pX, pY = tableau[i][j].getPos()
                        if(descente):
                            pY += offsetY
                            tableau[i][j].setPos(pX,pY)
                        else:
                            tableau[i][j].setPos(pX + decalageX, pY)
        if (vaisseau.isAlive() and self.__itsOver == False and self.__victoire == False):
            Fonctions.maFenetre.after(100, self.deplacementEnnemies, vaisseau)
    
    #def attaqueEnnemy(self,vaisseau):
    def resetLevel(self, vaisseau):
        '''Réinitialisation du niveau en cas de victoire ou défaite'''
        vaisseau.setVie(3)
        for i in range(len(Fonctions.liste_missile)):
            Fonctions.Canevas.delete(Fonctions.liste_missile[i].getImg())
        Fonctions.liste_missile.clear()
        self.__victoire = False
        if type(self.__labelScore) != type(None) : 
            self.__labelScore.pack_forget()
            vaisseau.setScore(0)
    
    def setupShield(self):
        '''Initialisation du tableau du bouclier'''
        from Bouclier import Bouclier
        global spriteShield, liste_rocher, pattern_rocher

        b_standart = Bouclier("Image rocher", 100, 100, 0)
        spriteShield = PhotoImage(file= str(b_standart.getImg()))
        liste_rocher = []
        x = Fonctions.Largeur
        nb_slot = x / spriteShield.width()
        pattern = [0,1,1,1,0]
        pattern_rocher = [pattern for i in range(int(nb_slot / len(pattern)))]
        pat = []

        for i in pattern_rocher:
            for j in i:
                pat.append(j)
        liste_rocher = [[None for i in range(len(pat))] for j in range(2)]
        for j in range(len(liste_rocher)):
            for j in range(len(liste_rocher[0])):
                if(pat[j] == 1):
                    roc = Bouclier("Image rocher", 25 + 25 * j, 450 + 25 * i, str(i)+str(j))
                    roc.afficherBouclier(spriteShield)
                    liste_rocher[i][j] = roc
        
    def setupHUD(self, vaisseau):
        '''Initialise l'interface du jeu comme les points de vie'''
        global spriteCoeur, tabCoeur, label_score
        
        spriteCoeur = PhotoImage(file = "Image Coeur")
        tabCoeur = []

        for i in range(vaisseau.getVie()):
            vaisseau.afficherVie(spriteCoeur, 800 - 30 * (i + 1), 30)
        sc = StringVar()
        self.__labelScore = Label(Fonctions.Canevas, bg = "white", textvariable = sc)
        self.affichageScore(vaisseau,sc)
        self.__labelScore.place(x = 5, y = 5, width = 100, height = 50)

    def affichageScore(self, vaisseau, sc):
        '''Affiche le score'''
        sc.set("Score : " + str(vaisseau.getScore()))
        Fonctions.maFenetre.after(200, self.affichageScore, vaisseau, sc)

    def victoire(self):
        '''Test si on a un cas de victoire'''
        global tableau
        self.__victoire = True 
        for i in range(len(tableau)):
            for j in range(len(tableau[0])):
                if type(tableau[i][j]) != type(None):
                    self.__victoire = False
        Fonctions.maFenetre.after(100, self.victoire)

    def finNiveau(self, vaisseau):
        '''Apparition d'une fenêtre en  cas de victoire'''
        if self.getVictoire() == True:
            if askyesno("Victoire", "Replay?"):
                self.setupLevel(vaisseau)
            else:
                Fonctions.maFenetre.destroy()
        elif self.getVictoire() == False and vaisseau.isAlive() == True and self.getItsOver() == False:
            Fonctions.maFenetre.after(100, self.finNiveau, vaisseau)

    





