from tkinter import *
from random import randint
from formes import *
from tkinter.colorchooser import askcolor
from tkinter import simpledialog

class ZoneAffichage(Canvas):
    def __init__(self, parent, w, h, c):

        Canvas.__init__(self, parent, width=w, height=h, bg=c)
        self.couleur1 = parent.couleurs[2]
        self.couleur2 = parent.couleurs[3]

        self.listeShape = [
        # Base, Poteau, Traverse, Corde
        Rectangle(self, 50,  270, 200,  26, self.couleur1),
        Rectangle(self, 87,   83,  26, 200, self.couleur1),
        Rectangle(self, 87,   70, 150,  26, self.couleur1),
        Rectangle(self, 183,  67,  10,  40, self.couleur1),
        # Tete, Tronc
        Rectangle(self, 188, 120,  20,  20, self.couleur2),
        Rectangle(self, 175, 143,  26,  60, self.couleur2),
        # Bras gauche et droit
        Rectangle(self, 133, 150,  40,  10, self.couleur2),
        Rectangle(self, 203, 150,  40,  10, self.couleur2),
        # Jambes gauche et droite
        Rectangle(self, 175, 205,  10,  40, self.couleur2),
        Rectangle(self, 191, 205,  10,  40, self.couleur2)
        ]

    def cachePendu(self):
        for f in self.listeShape:
            f.set_state("hidden")

    def dessinePiecePendu(self, i):
        if i<=len(self.listeShape):
            self.listeShape[i-1].set_state("normal")
    
    def effacePiecePendu(self, i):
        if i<=len(self.listeShape):
            self.listeShape[i-1].set_state("hidden")


class MonBoutonLettre(Button):
    def __init__(self, parent, fen, t):
        Button.__init__(self, master=parent, text=t, state=DISABLED)
        self.__fen=fen
        self.__lettre=t

    def cliquer(self):
        self.config(state=DISABLED)
        self.__fen.traitement(self.__lettre)

class MonBoutonCouleur(Button):
    def __init__(self, parent, fen, i):
        Button.__init__(self, master=parent, text="Choix couleur " + str(i+1))
        self.__i = i
        self.__fen = fen
    
    def cliquer(self):
        c = askcolor()
        if c[1]:
            self.__fen.couleurs[self.__i] = c[1]
            if self.__i == 0:
                self.__fen.configure(bg=self.__fen.couleurs[self.__i])
            elif self.__i == 1:
                self.__fen.zoneAffichage.configure(bg=self.__fen.couleurs[self.__i])
            elif self.__i == 2:
                for i in range(4):
                    self.__fen.zoneAffichage.listeShape[i].change_couleur(self.__fen.couleurs[self.__i])
            elif self.__i == 3:
                for i in range(4,10):
                    self.__fen.zoneAffichage.listeShape[i].change_couleur(self.__fen.couleurs[self.__i])



class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Jeu du pendu')
        self.couleurs = ["#2687bc", "#ec4062", "brown", "black"]
        self.nb_couleurs = len(self.couleurs)
        self.last_letters = []
        self.configure(bg=self.couleurs[0])

        self.__scores_file = "scores.txt"
        self.__pseudo = ""

        barreOutils = Frame(self)
        barreOutils.pack(side=TOP, padx=5, pady=5)
        newGameButton = Button(barreOutils, text ='Nouvelle partie', width=13)
        newGameButton.pack(side=LEFT, padx=5, pady=5)
        self.undoButton = Button(barreOutils, text ='Undo', width=13)
        self.undoButton.pack(side=LEFT, padx=5, pady=5)
        histButton = Button(barreOutils, text ='Historique', width=13)
        histButton.pack(side=LEFT, padx=5, pady=5)
        self.canUndoButton = Checkbutton(barreOutils, text="Autoriser Undo", width=13)
        self.canUndoButton.pack(side=LEFT, padx=5, pady=5)
        quitButton = Button(barreOutils, text ='Quitter', width=13)
        quitButton.pack(side=LEFT, padx=5, pady=5)

        self.zoneAffichage = ZoneAffichage(self, 320, 320, self.couleurs[1])
        self.zoneAffichage.pack(side=TOP, padx=5, pady=5)

        self.__lmot = Label(self, text='Mot :')
        self.__lmot.pack(side=TOP)

        self.__lscore = Label(self, text='Joueur : -')
        self.__lscore.pack(side=TOP)

        couleurFrame = Frame(self)
        couleurFrame.pack(side=TOP, padx=5, pady=5)
        self.__boutons_couleurs = []
        for i in range(self.nb_couleurs):
            self.__boutons_couleurs.append(MonBoutonCouleur(couleurFrame, self, i))

        for i in range(self.nb_couleurs):
            self.__boutons_couleurs[i].grid(row=1,column=i)

        clavier = Frame(self)
        clavier.pack(side=TOP, padx=5, pady=5)
        self.__boutons = []
        for i in range(26):
            t = chr(ord('A')+i)
            self.__boutons.append(MonBoutonLettre(clavier, self, t))

        for i in range(3):
            for j in range(7):
                self.__boutons[i*7+j].grid(row=i,column=j)
        for j in range(5):
            self.__boutons[21+j].grid(row=3,column=j+1)

        quitButton.config(command=self.destroy)
        self.undoButton.config(command=self.undo)
        newGameButton.config(command=self.nouvellePartie)
        histButton.config(command=self.afficheHistorique)
        self.canUndoButton.config(command=self.canUndo)
        for i in range(26):
            self.__boutons[i].config(command=self.__boutons[i].cliquer)

        for i in range(self.nb_couleurs):
            self.__boutons_couleurs[i].config(command=self.__boutons_couleurs[i].cliquer)

        self.__mot = ""
        self.__motAffiche = ""
        self.__mots = []
        self.__nbManques = 0

        self.chargeMots()

        self.nouvellePartie()

    def canUndo(self):
        if self.undoButton["state"]==NORMAL:
            self.undoButton.config(state=DISABLED)
        else:
            self.undoButton.config(state=NORMAL)

    def __demandePseudo(self):
        pseudo = simpledialog.askstring("Pseudo", "Entrez votre pseudo :", parent=self, initialvalue=self.__pseudo)
        
        if pseudo:
            self.__pseudo = pseudo
        else:
            self.__pseudo = "Anonyme"
        self.__lscore.config(text=f"Joueur : {self.__pseudo}")

    def afficheHistorique(self):
        fenetreHist = Toplevel(self)
        texte = f"Historique de {self.__pseudo}\n\n"
        total, total_score = 0, 0
        if self.__scores_file:
            with open(self.__scores_file, 'r') as f:
                for line in f:
                    parts = line.split(':')
                    if len(parts) == 3 and parts[0] == self.__pseudo:
                        mot, score = parts[1], float(parts[2])
                        total += 1
                        total_score += score
                        if score == 1.0:
                            resultat = "Gagné"
                        else:
                            resultat = "Perdu"
                        texte += f"{mot} - {score} - {resultat}\n"
        if total == 0:
            texte += "Aucune partie enregistrée."
        else:
            texte += f"\nParties : {total}  |  Moyenne : {total_score/total}"
        Label(fenetreHist, text=texte, padx=10, pady=10).pack()
        Button(fenetreHist, text="Fermer", command=fenetreHist.destroy).pack(pady=5)

    def chargeMots(self):
        f = open('mots.txt', 'r')
        s = f.read()
        self.__mots = s.split('\n')
        f.close()

    def undo(self):
        if len(self.last_letters)>0:
            l = self.last_letters[-1]
            self.__boutons[ord(l)-ord('A')].config(state=NORMAL)
            cpt = 0
            lettres = list(self.__motAffiche)
            for i in range(len(self.__mot)):
                if self.__mot[i]==l:
                    cpt +=1
                    lettres[i]= "*"

            self.__motAffiche = ''.join(lettres)

            if cpt ==0:
                self.__nbManques -= 1
                self.zoneAffichage.effacePiecePendu(self.__nbManques + 1)
            else:
                self.__lmot.config(text='Mot : ' + self.__motAffiche)
            self.last_letters.pop()

    def nouvellePartie(self):
        self.__demandePseudo()

        for i in range(26):
            self.__boutons[i].config(state=NORMAL)

        self.__mot = self.__mots[randint(0,len(self.__mots) - 1)]
        self.__motAffiche = len(self.__mot)*'*'
        self.__lmot.config(text='Mot : ' + self.__motAffiche)

        self.__nbManques = 0
        self.zoneAffichage.cachePendu()
        self.last_letters = []

    def traitement(self, lettre):
        self.last_letters.append(lettre)
        cpt = 0
        lettres = list(self.__motAffiche)
        for i in range(len(self.__mot)):
            if self.__mot[i]==lettre:
                cpt +=1
                lettres[i]=lettre

        self.__motAffiche = ''.join(lettres)

        if cpt ==0:
            self.__nbManques += 1
            self.zoneAffichage.dessinePiecePendu(self.__nbManques)
            if self.__nbManques >= 10:
                self.finPartie(False)
        else:
            self.__lmot.config(text='Mot : '+self.__motAffiche)
            if self.__mot == self.__motAffiche:
                self.finPartie(True)

    def finPartie(self, gagne):
        for b in self.__boutons:
            b.config(state=DISABLED)

        score = sum(1 for c in self.__motAffiche if c != '*') / len(self.__mot)
        with open(self.__scores_file, 'a') as f:
            f.write(f"{self.__pseudo}:{self.__mot}:{score}\n")

        if gagne :
            self.__lmot.config(text=self.__mot + ' - Bravo, vous avez gagné')
        else :
            self.__lmot.config(text='Vous avez perdu, le mot était : ' + self.__mot)


if __name__ == '__main__':
    fen = FenPrincipale()
    fen.mainloop()