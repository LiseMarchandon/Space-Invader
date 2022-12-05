from tkinter import Tk, Button, Label, StringVar, Frame, PhotoImage, Canvas

#section fonctions
def LancerJeu():
    #création du joueur sur l'interface graphique
    joueur = Canevas.create_image(PosX,PosY, image = chat)
    mechant = Canevas.create_image(PosXs,PosYs, image = souris)
    Canevas.focus_set()
    Canevas.bind('<Key>', MouvementJoueur())
    return 0

def MouvementJoueur(event):
    global PosX, PosY
    touche = event.keysym
    if touche == 'left':
        PosX -= 20
    if touche == 'right':
        PosX += 20
    Canevas.move(joueur,PosX)


MaFenetre = Tk()
MaFenetre.title('Space Invader')

MaFenetre.geometry('1000x850+400+100')

photo = PhotoImage(file="ciel.png")
chat = PhotoImage(file='chat2.png')
souris = PhotoImage(file='souris2.png')


FrameTitre = Frame(MaFenetre, bg ='navy', width=1000, height=100)

FrameTitre.pack(side = 'top', fill= 'x')
Label(FrameTitre, text = 'Space Invader').pack(padx=10, pady= 10)


FrameMenu = Frame (FrameTitre, bg='white')
FrameMenu.pack(side= 'right', padx = 10, pady = 10 )


boutonQuitter = Button(FrameMenu, fg = 'black', text ='Quitter', command = MaFenetre.destroy)
boutonQuitter.pack(side = 'right', padx=5, pady=5)


boutonRecommencer = Button(FrameMenu, fg = 'black', text ='Recommencer')
boutonRecommencer.pack(side = 'right', padx=5, pady=5)

boutonApropos = Button(FrameMenu, fg = 'black', text ='A propos')
boutonApropos.pack(side = 'right', padx=5, pady=5)

Label(FrameTitre, fg='black', text = 'Score :').pack(side = 'left', padx=10, pady= 10)
Label(FrameTitre, fg='black', text = 'Lives :').pack(side = 'left', padx=10, pady= 10)

FrameJeu = Frame (MaFenetre)
FrameJeu.pack()

Canevas = Canvas(FrameJeu, width=1000, height=700, bg='black')
Canevas.pack()
item= Canevas.create_image(0,0, anchor = 'nw', image=photo)

boutonCommencer = Button(FrameJeu, fg = 'black', text ='Commencer', command = LancerJeu)
boutonCommencer.pack()

#position initiale du joueur
PosX = 500
PosY = 650

#position initiale des mechants
PosXs = 500
PosYs = 50

MaFenetre.mainloop()

