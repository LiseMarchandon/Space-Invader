from tkinter import Tk, Button, Label, StringVar, Frame, PhotoImage, Canvas
from classejoueur import Joueur

class Interface :
    def __init__(self):
        self.maFenetre = Tk()
        self.maFenetre.title('Space Invader')
        self.maFenetre.geometry('1000x850+400+100')
        self.__photo = PhotoImage(file="ciel.png")
        self.__chat = PhotoImage(file='chat2.png')
        self.__souris = PhotoImage(file='souris2.png')
        
        

    def AffichageDebut(self):

        self.__FrameTitre = Frame(self.maFenetre, bg ='navy', width=1000, height=100)
        self.__FrameTitre.pack(side = 'top', fill= 'x')
        Label(self.__FrameTitre, text = 'Space Invader').pack(padx=10, pady= 10)
        Label(self.__FrameTitre, fg='black', text = 'Score :').pack(side = 'left', padx=10, pady= 10)
        Label(self.__FrameTitre, fg='black', text = 'Lives :').pack(side = 'left', padx=10, pady= 10)
        
        self.__FrameMenu = Frame(self.__FrameTitre, bg='white')
        self.__FrameMenu.pack(side= 'right', padx = 10, pady = 10 )

        self.__FrameJeu = Frame(self.maFenetre)
        self.__FrameJeu.pack()

        self.__boutonQuitter = Button(self.__FrameMenu , fg = 'black', text ='Quitter', command = self.maFenetre.destroy)
        self.__boutonRecommencer = Button(self.__FrameMenu , fg = 'black', text ='Recommencer')
        self.__boutonApropos = Button(self.__FrameMenu , fg = 'black', text ='A propos')

        self.__Canevas = Canvas(self.__FrameJeu, width=1000, height=700, bg='black')
        self.__Canevas.pack()
        self.__Canevas.create_image(0,0, anchor = 'nw', image=self.__photo)
        
        self.__boutonQuitter.pack(side = 'right', padx=5, pady=5)
        self.__boutonRecommencer.pack(side = 'right', padx=5, pady=5)
        self.__boutonApropos.pack(side = 'right', padx=5, pady=5)
        self.__boutonCommencer = Button(self.__FrameJeu, fg = 'black', text ='Commencer', command = self.LancementJeu)
        self.__boutonCommencer.pack()

        
    
    def LancementJeu(self):
        self.__joueur = Joueur(500,650) 
        self.__imagejoueur = self.__Canevas.create_image(500,650, image = self.__chat)
        imagemechant = self.__Canevas.create_image(500,50, image = self.__souris)

        self.Jeu()

    def Jeu(self):
        self.__Canevas.bind('<Left>', self.MouvementJoueurLi())
        self.__Canevas.bind('<Right>', self.MouvementJoueurRi())

        self.maFenetre.mainloop()
    
    def MouvementJoueurRi(self):
        self.__joueur.MouvementJoueurR()
        self.__positionx = self.__joueur.RecupPositionX()
        self.__positiony = self.__joueur.RecupPositionY()
        self.__Canevas.move(self.__joueur, self.__positionx,self.__positiony )
    
    def MouvementJoueurLi(self):
        self.__joueur.MouvementJoueurL()
        self.__positionx = self.__joueur.RecupPositionX()
        self.__positiony = self.__joueur.RecupPositionY()
        self.__Canevas.move(self.__joueur, self.__positionx,self.__positiony )




        
        



