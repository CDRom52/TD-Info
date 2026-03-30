from datetime import date

class Personne:
    def __init__(self,nom,prenom,adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        
    def set_nom(self,nom):
        self.__nom = nom
        
    def get_nom(self):
        return self.__nom
        
    def set_prenom(self,prenom):
        self.__prenom = prenom
        
    def get_prenom(self):
        return self.__prenom
        
    def set_adresse(self,adresse):
        self.__adresse = adresse
        
    def get_adresse(self):
        return self.__adresse
    
class Bibliotheque:
    def __init__(self, nom):
        self.__nom = nom
        self.__lecteurs = []
        self.__livres = []
        self.__emprunts = []
        self.__bibliothecaires = []
        self.__conservateur = None

    def get_nom(self):
        return self.__nom
        
    def ajout_lecteur(self,nom,prenom,adresse,numero):
        self.__lecteurs.append(Lecteur(nom,prenom,adresse,numero))
        
    def retrait_lecteur(self,numero):
        lecteur = self.chercher_lecteur_numero(numero)
        if lecteur is None:
            return False
        for e in self.__emprunts:
            if e.get_numero_lecteur()==numero:
                return False
        self.__lecteurs.remove(lecteur)
        return True                
                
    def ajout_livre(self,auteur,titre,numero,nb_total):
        self.__livres.append(Livre(auteur,titre,numero,nb_total))
    
    def retrait_livre(self,numero):
        livre = self.chercher_livre_numero(numero)
        if livre is None:
            return False
        for e in self.__emprunts:
            if e.get_numero_livre()==numero:
                return False
        self.__livres.remove(livre)
        return True        
        
    def chercher_lecteur_numero(self,numero):
        for l in self.__lecteurs:
            if l.get_numero() == numero:
                return l
        return None

    def chercher_lecteur_nom(self,nom,prenom):
        for l in self.__lecteurs:
            if l.get_nom() == nom and l.get_prenom() == prenom:
                return l
        return None    
        
    def chercher_livre_numero(self,numero):
        for l in self.__livres:
            if l.get_numero() == numero:
                return l
        return None

    def chercher_livre_titre(self,titre):
        for l in self.__livres:
            if l.get_titre() == titre:
                return l
        return None    
        
    def chercher_emprunt(self, numero_lecteur, numero_livre):
        for e in self.__emprunts:
            if e.get_numero_lecteur() == numero_lecteur and e.get_numero_livre() == numero_livre:
                return e
        return None

    def set_conservateur(self, conservateur):
        self.__conservateur = conservateur

    def get_conservateur(self):
        return self.__conservateur

    def ajout_bibliothecaire(self, nom, prenom, adresse, numero_emp):
        new_biblio = Bibliothecaire(nom, prenom, adresse, numero_emp)
        self.__bibliothecaires.append(new_biblio)

    def chercher_biblio_numero(self, numero_emp):
        for b in self.__bibliothecaires:
            if b.get_numero_emp() == numero_emp:
                return b
        return None

    def retrait_bibliothecaire(self, numero_emp):
        biblio = self.chercher_biblio_numero(numero_emp)
        if biblio:
            self.__bibliothecaires.remove(biblio)
            return True
        return False

    def affiche_bibliothecaires(self):
        print(f"--- Liste des bibliothécaires de {self.__nom} ---")
        for b in self.__bibliothecaires:
            print(b)
            print(b.get_nb_enregistrements())

    def emprunt_livre(self, numero_lecteur, numero_livre, numero_biblio):
        biblio = self.chercher_biblio_numero(numero_biblio)
        if biblio is None:
            print("Emprunt impossible : bibliothécaire non reconnu")
            return None

        livre = self.chercher_livre_numero(numero_livre)
        lecteur = self.chercher_lecteur_numero(numero_lecteur)
        
        if livre and lecteur and livre.get_nb_dispo() > 0:
            e = Emprunt(numero_lecteur, numero_livre, numero_biblio)
            self.__emprunts.append(e)
            livre.set_nb_dispo(livre.get_nb_dispo() - 1)
            lecteur.set_nb_emprunts(lecteur.get_nb_emprunts() + 1)
            biblio.set_nb_enregistrements(biblio.get_nb_enregistrements() + 1)
            return e
        else:
            print("Emprunt impossible : conditions non remplies")
            return None
        
    def retour_livre(self, numero_lecteur, numero_livre):
        e = self.chercher_emprunt(numero_lecteur, numero_livre)
        if e is not None:
            self.__emprunts.remove(e)
            lecteur = self.chercher_lecteur_numero(numero_lecteur)
            if lecteur is not None :
                lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()-1)
            livre = self.chercher_livre_numero(numero_livre)
            if livre is not None:
                livre.set_nb_dispo(livre.get_nb_dispo()+1)
            print('Retour effectue')
            return True
        else:
            print('Aucun emprunt ne correspond a ces informations')
            return False
            
    def affiche_lecteurs(self):
        for l in self.__lecteurs:
            print(l)

    def affiche_livres(self):
        for l in self.__livres:
            print(l)           
            
    def affiche_emprunts(self):
        for e in self.__emprunts:
            print(e)


class Emprunt:
    def __init__(self, numero_lecteur, numero_livre, numero_biblio):
        self.__numero_lecteur = numero_lecteur
        self.__numero_livre = numero_livre
        self.__numero_biblio = numero_biblio
        self.__date = date.isoformat(date.today())

    def get_numero_biblio(self):
        return self.__numero_biblio
    
    def get_numero_lecteur(self):
        return self.__numero_lecteur
        
    def get_numero_livre(self):
        return self.__numero_livre
        
    def get_date(self):
        return self.__date

    def __str__(self):
        return (f"Emprunt - Lecteur: {self.__numero_lecteur}, Livre: {self.__numero_livre}, "
                f"Numéro du bibliothécaire: {self.__numero_biblio}, Date: {self.__date}")

class Lecteur(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse)        
        self.__numero = numero
        self.__nb_emprunts = 0
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
        
    def set_nb_emprunts(self,nb_emprunts):
        self.__nb_emprunts = nb_emprunts
        
    def get_nb_emprunts(self):
        return self.__nb_emprunts
        
    def __str__(self):
        return 'Lecteur - Nom : {}, Prenom : {}, Adresse : {}, Numero : {}, Nb emprunts : {}'.format(self.get_nom(),self.get_prenom(),self.get_adresse(),self.__numero,self.__nb_emprunts)
    
class Livre:
    def __init__(self,titre,auteur,numero,nb_total):
        self.__titre = titre        
        self.__auteur = auteur
        self.__numero = numero
        self.__nb_total = nb_total
        self.__nb_dispo = nb_total

    def set_auteur(self,auteur):
        self.__auteur = auteur
        
    def get_auteur(self):
        return self.__auteur
        
    def set_titre(self,titre):
        self.__titre = titre
        
    def get_titre(self):
        return self.__titre
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
    
    def set_nb_total(self,nb_total):
        self.__nb_total = nb_total
        
    def get_nb_total(self):
        return self.__nb_total

    def set_nb_dispo(self,nb_dispo):
        self.__nb_dispo = nb_dispo
        
    def get_nb_dispo(self):
        return self.__nb_dispo
        
    def __str__(self):
        return 'Livre - Auteur : {}, Titre : {}, Numero : {}, Nb total : {}, Nb dispo : {}'.format(self.__auteur,self.__titre,self.__numero,self.__nb_total,self.__nb_dispo)

class Bibliothecaire(Personne):
    def __init__(self, nom, prenom, adresse, numero_emp):
        Personne.__init__(self, nom, prenom, adresse)
        self.__numero_emp = numero_emp
        self.__nb_enregistrements = 0

    def get_numero_emp(self):
        return self.__numero_emp
    
    def get_nb_enregistrements(self):
        return self.__nb_enregistrements
    
    def set_nb_enregistrements(self, nb):
        self.__nb_enregistrements = nb

    def __str__(self):
        return f"Bibliothécaire n°{self.__numero_emp} : {self.get_nom()} {self.get_prenom()}"

class Conservateur(Personne):
    def __init__(self, nom, prenom, adresse):
        Personne.__init__(self, nom, prenom, adresse)

    def __str__(self):
        return f"Conservateur : {self.get_nom()} {self.get_prenom()}"
    

"""
TEST
# Creation d'une bibliotheque
b = Bibliotheque('Bibliotheque ECL')
b.ajout_bibliothecaire("Cassette", "Hugo", "rue de la Paix", 1)
b.ajout_bibliothecaire("Favre-Bulle", "Romain", "rue de la Guerre", 2)
b.ajout_bibliothecaire("Pitt", "Brad", "rue de la Mort", 3)

c = Conservateur("Jean", "Jean", "rue de la Vie")
b.set_conservateur(c)



# Ajout de lecteurs
b.ajout_lecteur('Duval','Pierre','rue de la Paix',1)
b.ajout_lecteur('Dupond','Laurent','rue de la Gare',2)
b.ajout_lecteur('Martin','Marie','rue La Fayette',3)
b.ajout_lecteur('Dubois','Sophie','rue du Stade',4)

# Ajout de livres
b.ajout_livre('Le Pere Goriot','Honore de Balzac',101,2)
b.ajout_livre('Les Hauts de Hurlevent','Emilie Bronte',102,2)
b.ajout_livre('Le Petit Prince','Antoine de Saint Exupery',103,2)
b.ajout_livre('L\'Etranger','Albert Camus',104,2)

# Affichage des lecteurs et des livres
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()

# Recherches de lecteurs par numero
print('\n--- Recherche de lecteurs :')
print('-------------------------------')
lect = b.chercher_lecteur_numero(1)
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')

lect = b.chercher_lecteur_numero(6)
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')

# Recherches de lecteurs par nom
lect = b.chercher_lecteur_nom('Martin','Marie')
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')
    
lect = b.chercher_lecteur_nom('Le Grand','Paul')
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')

# Recherches de livres par numero
print('\n--- Recherche de livres :')
print('-------------------------------')
livre = b.chercher_livre_numero(101)
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

livre = b.chercher_livre_numero(106)
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

# Recherches de livres par titre
livre = b.chercher_livre_titre('Les Hauts de Hurlevent')
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

livre = b.chercher_livre_titre('Madame Bovarie')
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

# Quelques emprunts
print('\n--- Quelques emprunts :')
print('-------------------------------')
b.emprunt_livre(1,101, 1)
b.emprunt_livre(1,104, 2)
b.emprunt_livre(2,101, 3)
b.emprunt_livre(2,105, 2)
b.emprunt_livre(3,101, 3)
b.emprunt_livre(3,104, 2)
b.emprunt_livre(4,102, 1)
b.emprunt_livre(4,103, 2)

# Affichage des emprunts, des lecteurs et des livres
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()
print('\n--- Liste des bibliothécaires :')
print('-------------------------------')
b.affiche_bibliothecaires()

b.retrait_bibliothecaire(3)
print('\n--- Liste des bibliothécaires :')
print('-------------------------------')
b.affiche_bibliothecaires()


# Quelques retours de livres
print('\n--- Quelques retours de livres :')
print('-------------------------------')
b.retour_livre(1,101)
b.retour_livre(1,102)
b.retour_livre(3,104)
b.retour_livre(10,108)

# Affichage des emprunts, des lecteurs et des livres
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()



# Suppression de quelques livres
rep = b.retrait_livre(101)
if not rep:
    print('Retrait du livre impossible')
else:
    print('Retrait du livre effectue')

b.retour_livre(2,101)

rep = b.retrait_livre(101)
if not rep:
    print('Retrait du livre impossible')
else:
    print('Retrait du livre effectue')

# Suppression de quelques lecteurs
rep = b.retrait_lecteur(1)
if not rep:
    print('Retrait du lecteur impossible')
else:
    print('Retrait du lecteur effectue')

b.retour_livre(1,104)

rep = b.retrait_lecteur(1)
if not rep:
    print('Retrait du lecteur impossible')
else:
    print('Retrait du lecteur effectue')

# Affichage des emprunts, des lecteurs et des livres
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()
"""