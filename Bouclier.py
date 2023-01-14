'''
ce fichier a pour but de gérer les ilots boucliers du jeu
date de début: 08/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''
from tkinter import PhotoImage
import Fonctions

class Bouclier:
    
    def __init__(self, img, posX, posY, ident):

        """
        cette méthode initialise l'élément bouclie
        entrées: image du bouclier (ici des paniers), position selon l'axe de abscisses, position selon l'axe des y, un identifiant associer à chaque bouclier(ceci permettra de faciliter la destruction de chaque bouclier)
        sorties: pas de sorties
        """

        self._img = img
        self._posX = posX
        self._posY = posY
        self._ident = ident
        self._sprite = PhotoImage(file = str(self._img))
        
    def getPos(self):

        """
        cette méthode récupère la position du bouclier
        entrées: l'objet visé
        sorties: position selon l'axe des abscisses et l'axe des ordonnées sous forme de liste
        """

        return [self._posX, self._posY]

    def getImg(self):

        """
        cette méthode récupère l'image du bouclier mais contrairement à la méthode getSprite, cette méthode ne travaille pas avec l'interface tkinter
        entrées: l'objet visé
        sorties: image du bouclier sous forme de str
        """

        return self._img

    def getTaille(self):

        """
        cette méthode récupère la taille du bouclier
        entrées: l'objet visé
        sorties: nombre de boucliers par ligne et nombre de boucliers par colonne
        """

        return self._ligne, self._colonne

    def getSprite(self):

        """
        cette méthode récupère la photo du bouclier
        entrées: l'objet visé
        sorties: image du bouclier
        """

        return self._sprite
    
    def getIdent(self):

        """
        cette méthode récupère l'identifiant associé à chaque bouclier
        entrées: l'objet visé
        sorties: identifiant du premier bouclier sous forme d'un entier et les identifiants des boucliers suivants sous forme d'entiers
        """

        ident = self._ident
        return int(ident[0]),int(ident[1:])
        
    def setPos(self, x, y):
        
        """
        cette méthode permet de modifiers la position du bouclier
        entrées: l'objet visé, position selon x et selon y
        sorties: pas de sortie
        """

        self._posX = x
        self._posY = y

    def afficherBouclier(self, sprite):

        """
        cette méthode permet d'afficher une famille, un bloc de boucliers
        entrées: l'objet visé, image du bouclier
        sorties: pas de sortie
        """

        spriteShield = sprite
        img_shield = Fonctions.Canevas.create_image(self._posX ,self._posY , image = spriteShield)
        self._img = img_shield
        Fonctions.Canevas.image = spriteShield 