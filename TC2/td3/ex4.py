class Personne:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        print(self.nom)

class Club:
    def __init__(self, nom):
        self.nom = nom
        self.adherents = []
        self.activites = []

    def ajout_adherent(self, nom, num):
        self.adherents.append(Adherent(nom, num))

    def ajout_activite(self, nom):
        self.activites.append(Activite(nom))

class Adherent(Personne):

class Activite:
    