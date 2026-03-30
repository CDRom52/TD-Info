class Restaurant:
    def __init__(self, nom, cuisiniers, serveurs):
        self.nom = nom
        self.cuisiniers = cuisiniers
        self.serveurs = serveurs

    def __str__(self):
        print("restaurant " + self.nom)

class Personne:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        print(self.nom)

class Directeur(Personne):
    def __init__(self, nom, restaurants):
        Personne.__init__(self, nom)
        self.restaurants = restaurants

    def __str__(self):
        print("directeur " + self.nom)

class Cuisinier(Personne):
    def __init__(self, nom, restaurant):
        Personne.__init__(self, nom)
        self.restaurant = restaurant
        self.restaurant.cusiniers.append(self)

    def __str__(self):
        print("cuisinier " + self.nom)

class Serveur(Personne):
    def __init__(self, nom):
        Personne.__init__(self, nom)
        self.restaurant = None
        self.restaurant.serveurs.append(self)

    def __str__(self):
        print("serveur " + self.nom)

class Client(Personne):
    def __init__(self, nom):
        Personne.__init__(self, nom)
        self.restaurants = []
        self.plats = []

    def __str__(self):
        print("client " + self.nom)

class Plat:
    def __init__(self, nom, serveur, client, cuisinier):
        self.nom = nom
        self.serveur = serveur
        self.client = client
        self.cuisinier = cuisinier

    def __str__(self):
        print("plat " + self.nom)