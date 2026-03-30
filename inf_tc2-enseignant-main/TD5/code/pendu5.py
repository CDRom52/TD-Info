#pendu5.py
from tkinter import *
from random import randint
from formes import *

class ZoneAffichage(Canvas):
    def __init__(self, parent, w, h, c):

        Canvas.__init__(self, master=parent, width=w, height=h, bg=c)

        # Listes des formes du pendu, dans l'ordre du dessin
        self.__listeShape = []

        # Base, Poteau, Traverse, Corde
        self.__listeShape.append(Rectangle(self, 50,  270, 200,  26, "brown"))
        self.__listeShape.append(Rectangle(self, 87,  83,   26, 200, "brown"))
        self.__listeShape.append(Rectangle(self, 87,  70,  150,  26, "brown"))
        self.__listeShape.append(Rectangle(self, 183, 67,   10,  40, "brown"))
        # Tete, Tronc
        self.__listeShape.append(Ellipse(self,   188, 120,  20,  20, "black"))
        self.__listeShape.append(Rectangle(self, 175, 143,  26,  60, "black"))
        # Bras gauche, droit
        self.__listeShape.append(Rectangle(self, 133, 150,  40,  10, "black"))
        self.__listeShape.append(Rectangle(self, 203, 150,  40,  10, "black"))
        # Jambes gauche et droite
        self.__listeShape.append(Rectangle(self, 175, 205,  10,  40, "black"))
        self.__listeShape.append(Rectangle(self, 191, 205,  10,  40, "black"))

    def cachePendu(self):
        for f in self.__listeShape:
            f.set_state("hidden")

    def dessinePiecePendu(self, i):
        if i<=len(self.__listeShape):
            self.__listeShape[i-1].set_state("normal")

class MonBoutonLettre(Button):
    def __init__(self, parent, fen, t):
        Button.__init__(self, master=parent, text=t, state=DISABLED)
        self.__fen=fen
        self.__lettre=t

    def cliquer(self):
        self.config(state=DISABLED)
        self.__fen.traitement(self.__lettre)


class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Jeu du pendu')
        self.configure(bg="#2687bc")

        # La barre d'outils
        barreOutils = Frame(self)
        barreOutils.pack(side=TOP, padx=5, pady=5)
        newGameButton = Button(barreOutils, text ='Nouvelle partie', width=13)
        newGameButton.pack(side=LEFT, padx=5, pady=5)
        quitButton    = Button(barreOutils, text ='Quitter',         width=13)
        quitButton.pack(side=LEFT, padx=5, pady=5)

        # Le canvas pour le dessin du pendu
        self.__zoneAffichage = ZoneAffichage(self, 320, 320, "#ec4062")
        self.__zoneAffichage.pack(side=TOP, padx=5, pady=5)

        # Le mot à deviner
        self.__lmot = Label(self, text='Mot :')
        self.__lmot.pack(side=TOP)

        # Le clavier
        clavier = Frame(self)
        clavier.pack(side=TOP, padx=5, pady=5)
        self.__boutons = []
        for i in range(26):
            t = chr(ord('A')+i)
            self.__boutons.append(MonBoutonLettre(clavier, self, t))

        # Placement des boutons du clavier
        for i in range(3):
            for j in range(7):
                self.__boutons[i*7+j].grid(row=i,column=j)
        for j in range(5):
            self.__boutons[21+j].grid(row=3,column=j+1)

        # Commandes associées aux boutons
        quitButton.config(command=self.destroy)
        newGameButton.config(command=self.nouvellePartie)
        for i in range(26):
            self.__boutons[i].config(command=self.__boutons[i].cliquer)

        # initialisation des attributs
        self.__mot = ""
        self.__motAffiche= ""
        self.__mots= []
        self.__nbManques  = 0

        # Chargement du fichier de mots
        self.chargeMots()

        # On commence une nouvelle partie
        self.nouvellePartie()

    def chargeMots(self):
        f = open('mots.txt', 'r')
        s = f.read()
        self.__mots = s.split('\n')
        f.close()

    def nouvellePartie(self):

        # Boutons-lettres dégrisés
        for i in range(26):
            self.__boutons[i].config(state=NORMAL)

        # Nouveau mot à devnier et update
        self.__mot        = self.__mots[randint(0,len(self.__mots)-1)]
        self.__motAffiche = len(self.__mot)*'*'
        self.__lmot.config(text='Mot : '+self.__motAffiche)

        # on re-init le nbre de coups manqués et on efface le précédent dessin
        self.__nbManques = 0
        self.__zoneAffichage.cachePendu() #---> on cache le pendu en utilisant la couleur de fond

    def traitement(self, lettre):
        cpt = 0
        lettres = list(self.__motAffiche)
        for i in range(len(self.__mot)):
            if self.__mot[i]==lettre:
                cpt +=1
                lettres[i]=lettre

        self.__motAffiche = ''.join(lettres)

        if cpt ==0:
            self.__nbManques += 1
            self.__zoneAffichage.dessinePiecePendu(self.__nbManques) #---> Dessin de l'elt suivant
            if self.__nbManques >= 10:
                self.finPartie(False)
        else:
            self.__lmot.config(text='Mot : '+self.__motAffiche)
            if self.__mot == self.__motAffiche:
                self.finPartie(True)

    def finPartie(self, gagne):
        for b in self.__boutons:
            b.config(state=DISABLED)

        if gagne :
            self.__lmot.config(text=self.__mot+' - Bravo, vous avez gagné')
        else :
            self.__lmot.config(text='Vous avez perdu, le mot était : '+self.__mot)


if __name__ == '__main__':
    fen = FenPrincipale()
    fen.mainloop()
