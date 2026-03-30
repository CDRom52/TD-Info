class Personne:
	def __init__(self,nom):
		self.__nom = nom

	def get_nom(self):
		return self.__nom

class Adherent(Personne):
	def __init__(self,nom,num):
		Personne.__init__(self,nom)
		self.__numero = num

	def get_numero(self):
		return	self.__numero

class Activite:
	def __init__(self,n):
		self.__nom = n
		self.__adherents = []

	def get_nom(self):
		return self.__nom

	def ajout_adherent(self,a):
		self.__adherents.append(a)

	def affiche_adherents(self):
		print('Liste des adherents:')
		for a in self.__adherents:
			print('Nom : {} - Numero : {}'.format(a.get_nom(), a.get_numero()))

class Club:
	def __init__(self,n):
		self.__nom = n
		self.__adherents = []
		self.__activites = []

	def ajout_adherent(self,nom,num):
		self.__adherents.append(Adherent(nom,num))

	def ajout_activite(self,n):
		self.__activites.append(Activite(n))

	def associe(self,numAdherent,nomActivite):
		ac = None
		for a in self.__activites:
			if a.get_nom() == nomActivite:
				ac = a 
				break

		ad = None
		for a in self.__adherents:
			if a.get_numero() == numAdherent:
				ad = a 
				break

		if ac != None and ad != None :
			ac.ajout_adherent(ad)

	def affiche_activites(self):
		print('Liste des activites:')
		for a in self.__activites:
			print('- Nom :',a.get_nom())
			a.affiche_adherents()

if __name__ == '__main__':
	c = Club('Ecully')
	c.ajout_adherent('Paul',1)
	c.ajout_adherent('Marc',2)
	c.ajout_adherent('Marie',3)

	c.ajout_activite('Escalade')
	c.ajout_activite('Theatre')
	c.ajout_activite('Football')

	c.associe(1,'Theatre')
	c.associe(2,'Theatre')
	c.associe(3,'Theatre')

	c.associe(2,'Escalade')
	c.associe(3,'Escalade')

	c.affiche_activites()



