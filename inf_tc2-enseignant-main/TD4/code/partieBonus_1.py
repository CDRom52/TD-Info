from tkinter import *
from tkinter import colorchooser # doit être importé manuellement
from formes import *

class ZoneAffichage(Canvas):
    def __init__(self, master, largeur, hauteur):
        Canvas.__init__(self, master, width=largeur, height=hauteur)
        self.__formes = []
        self.__type_forme = 'rectangle'
        self.__couleur = 'brown'
        self.__forme_deplacee = None
    
    def selection_rectangle(self):
        self.__type_forme = 'rectangle'
    
    def selection_ellipse(self):
        self.__type_forme = 'ellipse'
    
    def selection_couleur(self):
        self.__couleur = colorchooser.askcolor()[1]
    
    def ajout_forme(self, x, y):
        # Notez qu'on aurait aussi pu ajouter ce code en méthodes de Rectangle/Ellipse.
        if self.__type_forme == 'rectangle':
            f = Rectangle(self, x-5, y-10, 10, 20, self.__couleur)
        elif self.__type_forme == 'ellipse':
            f = Ellipse(self, x, y, 5, 10, self.__couleur)
        self.__formes.append(f)
    
    def suppression_forme(self, x, y):
        for f in self.__formes[::-1]:
            if f.contient_point(x, y):
                self.__formes.remove(f)
                f.effacer()
                break
    
    def expand_shape(self, startx, starty, x, y):
        if len(self.__formes)>0:
            self.__formes[-1].redimension_par_points(startx, starty, x, y)
            self.__formes[-1].update_coord_shape()


class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        # arbre de scène
        self.configure(bg="grey")
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
        self.__canevas = ZoneAffichage(self, 600, 400)
        self.__canevas.pack(side=TOP, padx=10, pady=10)
        
        # commandes
        boutonRectangle.config(command=self.__canevas.selection_rectangle)
        boutonEllipse.config(command=self.__canevas.selection_ellipse)
        boutonCouleur.config(command=self.__canevas.selection_couleur)
        boutonQuitter.config(command=self.destroy)
        self.__canevas.bind("<Button-1>", self.clic_canevas)
        self.__canevas.bind("<Control-ButtonRelease-1>", self.control_clic_canevas)
        self.__scale_en_cours = False
        self.__dernier_x = 0
        self.__dernier_y = 0
        self.__canevas.bind("<ButtonRelease-1>", self.release_canevas)
        self.__canevas.bind("<B1-Motion>", self.drag_canevas)
    
    def clic_canevas(self, event):
        self.__dernier_x = event.x
        self.__dernier_y = event.y
    
    def control_clic_canevas(self, event):
        self.__canevas.suppression_forme(event.x, event.y)
    
    def release_canevas(self, event):
        if not self.__scale_en_cours:
            self.__canevas.ajout_forme(event.x, event.y)
        self.__scale_en_cours = False
    
    def drag_canevas(self, event):
        self.__canevas.expand_shape(self.__dernier_x, self.__dernier_y, event.x, event.y)
        self.__scale_en_cours = True

if __name__ == '__main__':
    fen = FenPrincipale()
    fen.mainloop()
