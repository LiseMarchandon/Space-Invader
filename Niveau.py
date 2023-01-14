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

    def __init__(self, ligne, colonne):

        '''
        cette méthode initialise l'objet "niveau"
        entrées: l'objet visé, ligne, colonne 
        sorties: pas de sortie
        '''

        self._ligne = ligne
        self._colonne = colonne
        self._itsOver = False
        self._label_score = None
        self._victoire = False
        self._tab_Special = []
    
    def getItsOver(self):

        '''
        cette méthode permet de savoir si le jeu est fini
        entrées: l'objet visé
        sorties: boolean
        '''
    
        return self._itsOver

    def getVictoire(self):

        '''
        cette méthode permet de savoir si le joueur a gagné
        entrées: l'objet visé
        sorties: boolean
        '''

        return self._victoire
    
    def setupLevel(self, vaisseau):

        '''
        cette méthode initialise les paramètre du niveau
        entrées: l'objet visé, le joueur 
        sorties: pas de sortie
        '''

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

        '''
        cette méthode gère la liste des ennemies
        entrées: l'objet visé, le joueur
        sorties: pas de sortie
        '''

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

        '''
        cette méthode gère le déplacement des ennemies
        entrées: l'objet visé, le joueur
        sorties: pas de sortie
        '''

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

        '''
        cette méthode permet aux ennemies de tirer alétoirement 
        entrées: l'objet visé, le joueur
        sorties: pas de sortie
        '''

        if(vaisseau.isAlive()):
            tirage = random.randint(0, self._colonne - 1)
            for i in range(self._ligne):
                if(type(tableau[tirage][self._ligne - i - 1]) != type(None)):
                    tableau[tirage][self._ligne - i - 1].attaque()
                    break
        if(vaisseau.isAlive() and self._itsOver == False and self._victoire == False):    
            Fonctions.maFenetre.after(500, self.attaqueEnnemy, vaisseau)
            
    def resetLevel(self, vaisseau):

        '''
        cette méthode réinitialise le niveau en cas de victoire ou défaite
        entrées: l'objet visé, le joueur 
        sorties: pas de sortie
        '''

        vaisseau.setVie(3)
        for i in range(len(Fonctions.L_missile)):
            Fonctions.Canevas.delete(Fonctions.L_missile[i].getImg())
        Fonctions.L_missile.clear()
        self._victoire = False
        if type(self._label_score) != type(None):
            self._label_score.pack_forget()
            vaisseau.setScore(0)
        
    def setupShield(self):

        '''
        cette méthode initialise la liste des boucliers
        entrées: l'objet visé
        sorties: pas de sortie
        '''
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

        '''
        cette méthode initialise l'interface du jeu ainsi que les points de vie 
        entrées: l'objet visé, le joueur
        sorties: pas de sortie
        '''

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

        '''
        cette méthode affiche le score
        entrées: l'objet visé, le joueur, le score sous forme d'un entier
        sorties: pas de sortie
        '''

        sc.set("Score : " + str(vaisseau.getScore()))
        Fonctions.maFenetre.after(200, self.affichageScore, vaisseau, sc)
        
    def victoire(self):

        '''
        cette méthode test si il s'agit d'une victoire
        entrées: l'objet visé
        sorties: pas de sortie
        '''

        global tableau
        self._victoire = True
        for i in range(len(tableau)):
            for j in range(len(tableau[0])):
                if type(tableau[i][j]) != type(None):
                    self._victoire = False
        Fonctions.maFenetre.after(100, self.victoire)
    
    def finNiveau(self, vaisseau):


        '''
        cette méthode permet d'afficher une nouvelle fenêtre en cas de victoire
        entrées: l'objet visé
        sorties: pas de sortie
        '''

        if self.getVictoire() == True:
            if askyesno("Victoire", "Voulez-vous rejouer ?"):
                self.setupLevel(vaisseau)
            else:
                Fonctions.maFenetre.destroy()
        elif self.getVictoire() == False and vaisseau.isAlive() == True and self.getItsOver() == False:
            Fonctions.maFenetre.after(100, self.finNiveau, vaisseau)

    def specialEnnemy(self):

        '''
        cette méthode permet d'afficher l'ennemi special qui rapporte plus de points
        entrées: l'objet visé
        sorties: pas de sortie
        '''

        global spriteSpecial
        special = Ennemie('Special', "sourisboss.png", 82, 100, 40, 150)
        spriteSpecial = PhotoImage(file = str(special.getImg()))
        special.affichageEnnemy(spriteSpecial)
        self._tab_Special.append(special)
        Fonctions.maFenetre.after(100, self.depSpecial, special, spriteSpecial, True, 0)
        
    def depSpecial(self, special, sprite, direction, compteur):

        '''
        cette méthode gère le déplacement de l'ennemie spécial et le fait apparaître quelques secondes
        entrées: l'objet visé, l'ennemie special, photo de l'ennemi special, boolean = True pour savoir la direction de déplacement de l'ennemie, compteur du temps
        sorties: pas de sortie
        '''

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