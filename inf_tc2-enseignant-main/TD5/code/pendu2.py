#pendu2.py
from tkinter import *
from random import randint

class ZoneAffichage(Canvas):
	def __init__(self, parent, w, h, c):
		Canvas.__init__(self, master=parent, width=w, height=h, bg=c)

class FenPrincipale(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Jeu du pendu')
		self.configure(bg="#2687bc")
		
		# La barre d'outils
		barreOutils   = Frame(self)
		newGameButton = Button(barreOutils, text ='Nouvelle partie', width=13)
		quitButton    = Button(barreOutils, text ='Quitter',         width=13)
		
		# Le canvas pour le dessin du pendu
		self.__zoneAffichage = ZoneAffichage(self, 320, 320, "#ec4062")
		
		# Le mot à deviner
		self.__lmot = Label(self, text='Mot :')
		
		# Le clavier
		clavier = Frame(self)
		self.__boutons = []        
		for i in range(26):
			t = chr(ord('A')+i)
			self.__boutons.append(Button(clavier, text=t))
		
		# Placement des élts
		barreOutils.pack(side=TOP, padx=5, pady=5)
		newGameButton.pack(side=LEFT, padx=5, pady=5)
		quitButton.pack(side=LEFT, padx=5, pady=5)
		self.__zoneAffichage.pack(side=TOP, padx=5, pady=5)
		self.__lmot.pack(side=TOP)
		clavier.pack(side=TOP, padx=5, pady=5)
		for i in range(3):
			for j in range(7):
				self.__boutons[i*7+j].grid(row=i,column=j)		
		for j in range(5):
			self.__boutons[21+j].grid(row=3,column=j+1)

		# Commandes associées aux boutons
		quitButton.config(command=self.destroy)

if __name__ == '__main__':
	fen = FenPrincipale()
	fen.mainloop()
