'''
ce fichier a pour but de gérer le joueur 
date de début: 05/12/2022
MARIOTTE Mélanie & MARCHANDON Lise
To Do: 
'''

import Fonctions
import Niveau


class Vaisseau:

    def __init__(self,nom,vie,photo):

        """
        cette méthode initialise l'objet joueur
        entrées: l'objet visé, nom, nombre de vies, photo du joueur (pas la personne en question mdr)
        sorties: pas de sortie
        """

        self.__vie = vie 
        self.__nom = nom        
        self.__image = photo
        self.__coeur = None
        self.__score = 0

    def getImg(self):

        """
        cette méthode récupère l'image du joueur
        entrées: l'objet visé
        sorties: image du joueur (dans notre cas c'est un chat)
        """

        return self.__image
    
    def getScore(self):

        """
        cette méthode récupère le score du joueur
        entrées: l'objet visé
        sorties: score sous forme d'un entier
        """

        return self.__score
    
    def getVie(self):

        """
        cette méthode récupère la vie du joueur
        entrées: l'objet visé
        sorties: nombre de vies du joueur
        """

        return self.__vie
    
    def setScore(self, score):

        """
        cette méthode permet de modifier le score 
        entrées: l'objet visé et le score
        sorties: nouvelle valeur du score
        """

        self.__score = score
    
    def setVie(self, vie):

        """
        cette méthode permet de modifier le nombre de vies du joueur 
        entrées: l'objet visé et le nombre de vies
        sorties: nombres de vies restantes
        """

        self.__vie = vie
    
    '''Fonction qui détermine si le joueur est encore en vie'''

    def isAlive(self):

        """
        cette méthode permet de déterminer si le joueur est encore en vie 
        entrées: l'objet visé
        sorties: entier différent de 0
        """

        return self.__vie != 0
    
    def afficherVie(self,sprite, posX, posY):

        """
        cette méthode permet d'afficher le coeurs qui illustrent les vies du joueur
        entrées: l'objet visé, image du couer prêt pour l'interface tkinter, positions selon l'axe des abscisses et selon l'axe des ordonnées 
        sorties: pas de sortie
        """

        spriteCoeur = sprite
        image_Coeur = Fonctions.Canevas.create_image(posX, posY, image = spriteCoeur)
        self.__coeur = image_Coeur
        Fonctions.Canevas.image = spriteCoeur
        Niveau.tabCoeur.append(image_Coeur)


