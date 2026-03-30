from tkinter import *
from tkinter import colorchooser, messagebox, simpledialog
from random import randint
import os
from formes import *

class ZoneAffichage(Canvas):
    def __init__(self, parent, w, h, c):
        Canvas.__init__(self, master=parent, width=w, height=h, bg=c)
        self.listeShape = [
            # Base, Poteau, Traverse, Corde
            Rectangle(self, 50,  270, 200,  26, "brown"),
            Rectangle(self, 87,   83,  26, 200, "brown"),
            Rectangle(self, 87,   70, 150,  26, "brown"),
            Rectangle(self, 183,  67,  10,  40, "brown"),
            # Tete, Tronc
            Rectangle(self, 188, 120,  20,  20, "black"),
            Rectangle(self, 175, 143,  26,  60, "black"),
            # Bras gauche et droit
            Rectangle(self, 133, 150,  40,  10, "black"),
            Rectangle(self, 203, 150,  40,  10, "black"),
            # Jambes gauche et droite
            Rectangle(self, 175, 205,  10,  40, "black"),
            Rectangle(self, 191, 205,  10,  40, "black")
        ]

    def cachePendu(self):
        for f in self.__listeShape:
            f.set_state("hidden")

    def dessinePiecePendu(self, i):
        if 0 < i <= len(self.__listeShape):
            self.__listeShape[i-1].set_state("normal")
        elif i == 0:
            self.cachePendu()

class MonBoutonLettre(Button):
    def __init__(self, parent, fen, t):
        Button.__init__(self, master=parent, text=t, state=DISABLED)
        self.__fen = fen
        self.__lettre = t

    def cliquer(self):
        self.__fen.traitement(self.__lettre)

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Jeu du Pendu Pro')
        
        self.__historique = []
        self.__pseudo = ""
        self.__scores_file = "scores.txt"
        
        self.config(bg="#2687bc")
        
        self.__setup_menu()

        barreOutils = Frame(self)
        barreOutils.pack(side=TOP, padx=5, pady=5)
        
        Button(barreOutils, text='Nouvelle partie', command=self.nouvellePartie).pack(side=LEFT, padx=5)
        self.__btnUndo = Button(barreOutils, text='Undo (Triche!)', command=self.undo, state=DISABLED)
        self.__btnUndo.pack(side=LEFT, padx=5)
        Button(barreOutils, text='Quitter', command=self.destroy).pack(side=LEFT, padx=5)

        self.__zoneAffichage = ZoneAffichage(self, 320, 320, "#ec4062")
        self.__zoneAffichage.pack(side=TOP, padx=5, pady=5)

        self.__lmot = Label(self, text='Mot :', font=("Helvetica", 14, "bold"))
        self.__lmot.pack(side=TOP, pady=10)

        clavier = Frame(self)
        clavier.pack(side=TOP, padx=5, pady=5)
        self.__boutons = {}
        for i in range(26):
            t = chr(ord('A')+i)
            btn = MonBoutonLettre(clavier, self, t)
            btn.config(command=btn.cliquer)
            self.__boutons[t] = btn
            
            # Placement grid
            row, col = (i // 7, i % 7) if i < 21 else (3, (i-21) + 1)
            btn.grid(row=row, column=col, sticky="nsew")

        self.chargeMots()
        self.demanderPseudo() # Bonus
        self.nouvellePartie()

    def __setup_menu(self):
        menu_bar = Menu(self)
        menu_options = Menu(menu_bar, tearoff=0)
        menu_options.add_command(label="Changer couleur fond", command=self.choisir_couleur_fond)
        menu_options.add_command(label="Changer couleur dessin", command=self.choisir_couleur_canvas)
        menu_options.add_separator()
        menu_options.add_command(label="Voir Historique Scores", command=self.afficher_scores)
        menu_bar.add_cascade(label="Options & Apparence", menu=menu_options)
        self.config(menu=menu_bar)

    def choisir_couleur_fond(self):
        color = colorchooser.askcolor(title="Choisir couleur de fond")[1]
        if color: self.configure(bg=color)

    def choisir_couleur_canvas(self):
        color = colorchooser.askcolor(title="Choisir couleur du Canvas")[1]
        if color: self.__zoneAffichage.configure(bg=color)

    def demanderPseudo(self):
        self.__pseudo = simpledialog.askstring("Pseudo", "Entrez votre pseudo :")
        if not self.__pseudo: self.__pseudo = "Anonyme"

    def chargeMots(self):
        try:
            with open('mots.txt', 'r') as f:
                self.__mots = [line.strip().upper() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            self.__mots = ["PYTHON", "TKINTER", "ORDINATEUR", "PENDU"]

    def nouvellePartie(self):
        self.__historique = []
        self.__btnUndo.config(state=NORMAL)
        for b in self.__boutons.values():
            b.config(state=NORMAL)

        self.__mot = self.__mots[randint(0, len(self.__mots)-1)].upper()
        self.__motAffiche = len(self.__mot) * '*'
        self.__nbManques = 0
        self.__lmot.config(text='Mot : ' + self.__motAffiche)
        self.__zoneAffichage.cachePendu()

    def traitement(self, lettre):
        # Sauvegarde pour le Undo (Exo 8)
        etat_actuel = {
            'motAffiche': self.__motAffiche,
            'nbManques': self.__nbManques,
            'lettre': lettre
        }
        self.__historique.append(etat_actuel)

        self.__boutons[lettre].config(state=DISABLED)
        
        if lettre in self.__mot:
            nouveau_mot = list(self.__motAffiche)
            for i, char in enumerate(self.__mot):
                if char == lettre:
                    nouveau_mot[i] = lettre
            self.__motAffiche = "".join(nouveau_mot)
            self.__lmot.config(text='Mot : ' + self.__motAffiche)
        else:
            self.__nbManques += 1
            self.__zoneAffichage.dessinePiecePendu(self.__nbManques)

        self.verifier_fin()

    def undo(self):
        if not self.__historique: return
        
        dernier_etat = self.__historique.pop()
        
        # Restaurer l'affichage
        self.__motAffiche = dernier_etat['motAffiche']
        self.__nbManques = dernier_etat['nbManques']
        self.__boutons[dernier_etat['lettre']].config(state=NORMAL)
        
        self.__lmot.config(text='Mot : ' + self.__motAffiche)
        # Redessiner le pendu (on cache tout et on redessine jusqu'au niveau actuel)
        self.__zoneAffichage.cachePendu()
        for i in range(1, self.__nbManques + 1):
            self.__zoneAffichage.dessinePiecePendu(i)

    def verifier_fin(self):
        if self.__mot == self.__motAffiche:
            self.finPartie(True)
        elif self.__nbManques >= 10:
            self.finPartie(False)

    def finPartie(self, gagne):
        self.__btnUndo.config(state=DISABLED)
        for b in self.__boutons.values():
            b.config(state=DISABLED)

        # Calcul du score (Bonus)
        caracteres_trouves = len([c for c in self.__motAffiche if c != '*'])
        score = caracteres_trouves / len(self.__mot)
        
        resultat = "GAGNÉ" if gagne else "PERDU"
        self.__lmot.config(text=f"{self.__mot} - {resultat} (Score: {score:.2f})")
        
        self.sauvegarder_score(score)

    def sauvegarder_score(self, score):
        with open(self.__scores_file, "a") as f:
            f.write(f"{self.__pseudo};{self.__mot};{score:.2f}\n")

    def afficher_scores(self):
        if not os.path.exists(self.__scores_file):
            messagebox.showinfo("Scores", "Aucun historique disponible.")
            return
        with open(self.__scores_file, "r") as f:
            content = f.read()
        
        # Fenêtre simple pour afficher les scores
        top = Toplevel(self)
        top.title("Historique des scores")
        text = Text(top, width=40, height=15)
        text.insert(END, "Pseudo ; Mot ; Score\n" + "-"*30 + "\n")
        text.insert(END, content)
        text.config(state=DISABLED)
        text.pack()

if __name__ == '__main__':
    FenPrincipale().mainloop()