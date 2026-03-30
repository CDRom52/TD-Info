from lecteur import *
from emprunt import *
from livre import *

class Bibliotheque:
    def __init__(self,nom):
        self.__nom = nom
        self.__lecteurs = []
        self.__livres = []
        self.__emprunts = []
        
    def get_nom(self):
        return self.__nom
        
    def ajout_lecteur(self,nom,prenom,adresse,numero):
        self.__lecteurs.append(Lecteur(nom,prenom,adresse,numero))
        
    def retrait_lecteur(self,numero):
        lecteur = self.chercher_lecteur_numero(numero)
        if lecteur == None:
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
        if livre == None:
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

    def emprunt_livre(self, numero_lecteur, numero_livre):
        livre = self.chercher_livre_numero(numero_livre)
        if livre == None:
            print('Emprunt impossible : livre inexistant')
            return None
            
        if livre.get_nb_dispo() == 0:
            print('Emprunt impossible : plus d\'exemplaires disponibles')
            return None
            
        lecteur = self.chercher_lecteur_numero(numero_lecteur)
        if lecteur == None:
            print('Emprunt impossible : lecteur inexistant')
            return None
        e = self.chercher_emprunt(numero_lecteur, numero_livre)
        if e != None:
            print('Emprunt impossible : deja en cours')
            return None

        self.__emprunts.append(Emprunt(numero_lecteur, numero_livre))
        livre.set_nb_dispo(livre.get_nb_dispo()-1)
        lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
        return self.__emprunts[-1]

    def retour_livre(self, numero_lecteur, numero_livre):
        e = self.chercher_emprunt(numero_lecteur, numero_livre)
        if e != None:
            self.__emprunts.remove(e)
            lecteur = self.chercher_lecteur_numero(numero_lecteur)
            if lecteur != None : lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()-1)
            livre = self.chercher_livre_numero(numero_livre)
            if livre != None: livre.set_nb_dispo(livre.get_nb_dispo()+1)
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