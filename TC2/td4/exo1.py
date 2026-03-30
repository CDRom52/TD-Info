from tkinter import *
from random import randint

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        # paramètres de la fenêtre
        self.title('Tirage aléatoire')
        self.geometry('300x100+400+400')
        
        # constitution de l'interface
        boutonLancer = Button(self, text='Tirage')
        boutonLancer.pack(side=LEFT, padx=5, pady=5)
        self.__texteResultat = StringVar()
        labelResultat = Label(self, textvariable=self.__texteResultat, bg = "red")
        labelResultat.pack(side=LEFT, padx=5, pady=5)
        boutonQuitter = Button(self, text='Quitter')
        boutonQuitter.pack(side=LEFT, padx=5, pady=5)
        
        # association des widgets aux fonctions
        boutonLancer.config(command=self.tirage) # appel "callback" (pas de parenthèses !)
        boutonQuitter.config(command=self.destroy)  # idem
    
    # tire un entier au hasard et l'affiche dans self.__texteResultat
    def tirage(self):
        nb = randint(1, 100)
        self.__texteResultat.set('Nombre : ' + str(nb))


if __name__ == '__main__':
    app = FenPrincipale()
    app.mainloop()

"""
Réponses questions
#1  L'interface contient 4 éléments : la fenêtre, les 2 boutons, le résultat.
#2 Lorsqu'on clique sur le bouton tirage, on obtient un nombre au hasard entre 1 et 100, qui est affiché dans la fenêtre.
#3 Pour inverser les positions des 2 boutons, on change l'ordre dans lequel ils sont créés.
#4 Pour augmenter les espaces autour du label, on modifie padx.
#5 Pour colorier le texte du label, on ajoute un argument dans la création de l'objet label.
"""