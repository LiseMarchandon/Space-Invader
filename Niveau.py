'''
ce fichier a pour but de regrouper les Fonctions générales du jeu 
date de début: 08/01/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter import PhotoImage, Label, StringVar
from tkinter.messagebox import askyesno
import Fonctions 
import random
from Ennemie import Ennemie

class Niveau:

    '''Initialisation de l'objet niveau'''

    def __init__(self, ligne, colonne):
        self.__ligne = ligne
        self.__colonne = colonne
        self.__itsOver = False
        self.__label_score = None
        self.__victoire = False
        self.__tab_Special = []
    
    '''Fonctions permettant de récupérer les attributs de l'objet'''

    def getItsOver(self):
        '''
        La fonction renvoie True ou False pour vérifier si la partie est finie
        entrée : 
        sorties : True ou False 
        '''
        return self.__itsOver
    
    def getVictoire(self):
        '''
        La fonction renvoie True ou False pour vérifier si la partie est finie
        entrée : 
        sorties : True ou False 
        '''
        return self.__victoire
    
    def setupLevel(self, vaisseau):

        '''
        La fonction initialise les paramètres du niveau
        entrée : le joueur en question
        sorties : pas de sortie
        '''

        self.resetLevel(vaisseau)
        Fonctions.Canevas.bind("<KeyPress>", Fonctions.Clavier)
        self.setupEnnemies(vaisseau)
        self.setupShield()
        self.attaqueEnemy(vaisseau)
        self.setupHUD(vaisseau)
        self.specialEnnemy()
        self.victoire()
        self.finNiveau(vaisseau)
        Fonctions.gameOver(vaisseau, self)
        if (len(Fonctions.L_missile)!= 0):
            Fonctions.gestionMissile(vaisseau, self)
    
    def setupEnnemies(self, vaisseau):

        '''
        La fonction gère le tableau (liste) des ennemies
        entrée : le joueur en question
        sorties : pas de sortie 
        '''

        from Ennemie import Ennemie
        global tableau, spriteEnnemy, compteurX, compteurY, deplacementDroite, offsetX, offsetY
        
        compteurX = 0 
        deplacementDroite = True 
        tableau = [[0 for i in range(self.__ligne)] for i in range(self.__colonne)] 
        ennemyBase = Ennemie("test","souris2.png", 0, 0, 0, 25)
        spriteEnnemy = PhotoImage(file = str(ennemyBase.getImg()))
        offsetX = spriteEnnemy.width()
        offsetY = spriteEnnemy.height()
        separationX = 50
        separationY = 70
        for i in range(self.__colonne):
            for j in range(self.__ligne):
                posX = offsetX + separationX * i
                posY = offsetY + separationY * j
                ennemy = Ennemie('Alien'+ str(i)+str(j), "souris2.png", str(i)+str(j), posX, posY, 25)
                ennemy.affichageEnnemy(spriteEnnemy)
                tableau[i][j] = ennemy
        self.deplacementEnnemies(vaisseau)
    
    def deplacementEnnemies(self, vaisseau):

        '''
        La fonction gère le déplacement des ennemies
        entrée : le joueur en question
        sorties :  pas de sortie 
        '''

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
    
    def attaqueEnnemy(self,vaisseau):

        '''
        La fonction permet de générer des tirs aléatoires de la part des ennemies
        entrée : le joueur en question
        sorties :  pas de sortie
        '''

        if(vaisseau.isAlive()):
            tirage = random.randint(0, self.__colonne - 1)
            for i in range(self.__ligne):
                if(type(tableau[tirage][self.__ligne - i - 1]) != type(None)):
                    tableau[tirage][self.__ligne - i - 1].attaque()
                    break 
        if(vaisseau.isAlive() and self.__itsOver == False and self.__victoire == False):
            Fonctions.maFenetre.after(500, self.attaqueEnnemy, vaisseau)


    def resetLevel(self, vaisseau):

        '''
        La fonction réinitialise le niveau en cas de victoire ou défaite 
        entrée : le joueur en question
        sorties : pas de sortie
        '''

        vaisseau.setVie(3)
        for i in range(len(Fonctions.L_missile)):
            Fonctions.Canevas.delete(Fonctions.L_missile[i].getImg())
        Fonctions.L_missile.clear()
        self.__victoire = False
        if type(self.__label_score) != type(None) : 
            self.__label_score.pack_forget()
            vaisseau.setScore(0)
    
    def setupShield(self):

        '''
        La fonction initialise le tableau (liste) des obstacles, ici ce sont des paniers
        entrée : 
        sorties :  
        '''
        
        from Bouclier import Bouclier
        global spriteShield, L_rocher, pattern_rocher

        b_standart = Bouclier("panier.png", 100, 100, 0)
        spriteShield = PhotoImage(file= str(b_standart.getImg()))
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
                    roc = Bouclier("panier.png", 25 + 25 * j, 450 + 25 * i, str(i)+str(j))
                    roc.afficherBouclier(spriteShield)
                    L_rocher[i][j] = roc
        
    def setupHUD(self, vaisseau):

        '''
        La fonction initialise l'interface du jeu et les points de vie 
        entrée : le joueur en question
        sorties :  pas de sortie
        '''

        global spriteCoeur, tabCoeur, label_score
        
        spriteCoeur = PhotoImage(file = "vie.png")
        tabCoeur = []

        for i in range(vaisseau.getVie()):
            vaisseau.afficherVie(spriteCoeur, 800 - 30 * (i + 1), 30)
        sc = StringVar()
        self.__label_score = Label(Fonctions.Canevas, bg = "white", textvariable = sc)
        self.affichageScore(vaisseau,sc)
        self.__label_score.place(x = 5, y = 5, width = 100, height = 50)

    def affichageScore(self, vaisseau, sc):

        '''
        La fonction permet d'afficher le score 
        entrée : le joueur en question
        sorties :  
        '''

        sc.set("Score : " + str(vaisseau.getScore()))
        Fonctions.maFenetre.after(200, self.affichageScore, vaisseau, sc)


    def victoire(self):

        '''
        La fonction test si on a un cas de victoire
        entrée : 
        sorties : pas de sortie
        '''

        global tableau

        self.__victoire = True 
        for i in range(len(tableau)):
            for j in range(len(tableau[0])):
                if type(tableau[i][j]) != type(None):
                    self.__victoire = False
        Fonctions.maFenetre.after(100, self.__victoire)

    def finNiveau(self, vaisseau):

        '''
        La fonction permet d'afficher une fenêtre en cas de victoire
        entrée : le joueur en question
        sorties :  
        '''

        if self.getVictoire() == True:
            if askyesno("Victoire", "Voulez-vous rejouer?"):
                self.setupLevel(vaisseau)
            else:
                Fonctions.maFenetre.destroy()
        elif self.getVictoire() == False and vaisseau.isAlive() == True and self.getItsOver() == False:
            Fonctions.maFenetre.after(100, self.finNiveau, vaisseau)
    
    def specialEnnemy(self):

        '''
        La fonction fait apparaître l'ennemi special (gros rat) qui quand est touché rapporte plus de points
        entrée : 
        sorties :  
        '''

        global spriteSpecial

        special = Ennemie('Special', 'sourisboss.png', 82, 100, 40, 150)
        spriteSpecial = PhotoImage(file = str(special.getImg()))
        special.affichageEnnemy(spriteSpecial)
        self._tab_Special.append(special)
        Fonctions.maFenetre.after(100, self.depSpecial, special, spriteSpecial, True, 0)


    def depSpecial(self, special, sprite, direction, compteur):

        '''
        La fonction gère le déplacement de l'ennemi special et le fait apparâitre quelques secondes
        entrée : l'ennemi special, la direction de son déplacement (droite ou gauche), compteur qui permet de définir le temps d'apparition, sprite qui récupère l'image du méchant spécial
        sorties :  
        '''

        pX, pY = special.getPos()
        versDroite = direction
        if pX + sprite.width() / 2 < Fonctions.Largeur and versDroite == True:
            versDroite = False
        elif pX - sprite.width() / 2 < 0 and versDroite == False:
            versDroite = False
        if(versDroite):
            pX += 10 
        else:
            pX -= 10
        compteur += 1
        special.setPos(pX,pY)
        if(compteur >= 240):
            Fonctions.Canevas.delete(str(special.getImg()))
        Fonctions.maFenetre.after(50, self.depSpecial, special, sprite, versDroite, compteur)



    





