from tkinter import Tk, Button, Label, StringVar, Frame, PhotoImage

MaFenetre = Tk()
MaFenetre.title('Space Invader')

MaFenetre.geometry('1000x800+400+200')

photo = PhotoImage(file="ciel-étoile.jpg")

FrameMenu = Frame (MaFenetre)
FrameMenu.pack(side= 'top', width = 5, height = 5 )





MaFenetre.mainloop()