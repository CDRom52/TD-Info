from tkinter import *

class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="grey")
        
        # disposition des composants de l'interface
        barreOutils = Frame(self)
        barreOutils.pack(side=TOP)
        
        boutonRectangle = Button(barreOutils, text="Rectangle")
        boutonRectangle.pack(side=LEFT, padx=5, pady=5)
        boutonEllipse = Button(barreOutils, text="Ellipse")
        boutonEllipse.pack(side=LEFT, padx=5, pady=5)
        boutonCouleur = Button(barreOutils, text="Couleur")
        boutonCouleur.pack(side=LEFT, padx=5, pady=5)
        boutonQuitter = Button(barreOutils, text="Quitter")
        boutonQuitter.pack(side=LEFT, padx=5, pady=5)
        
        canevas = ZoneAffichage(self, 600, 400)
        canevas.pack(side=TOP, padx=10, pady=10)

if __name__ == "__main__":
    fen = FenPrincipale()
    fen.mainloop()
