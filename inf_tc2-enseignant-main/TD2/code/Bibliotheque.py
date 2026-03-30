# -*- coding: utf-8 -*-
"""

@author: dellandrea
"""
from lecteur import *
from livre import *
from emprunt import *
    
      
# ***** classe Bibliotheque *****
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
        # On cherche le lecteur
        lecteur = self.chercher_lecteur_numero(numero)
        if lecteur == None:
            return False
        # On verifie qu'il n'a pas d'emprunt en cours
        for e in self.__emprunts:
            if e.get_numero_lecteur()==numero:
                return False
        # On peut ici retirer le lecteur de la liste
        self.__lecteurs.remove(lecteur)
        return True                
                
    def ajout_livre(self,auteur,titre,numero,nb_total):
        self.__livres.append(Livre(auteur,titre,numero,nb_total))
    
    def retrait_livre(self,numero):
        # On cherche le livre
        livre = self.chercher_livre_numero(numero)
        if livre == None:
            return False
        # On verifie que le livre n'est pas en cours d'emprunt
        for e in self.__emprunts:
            if e.get_numero_livre()==numero:
                return False
        # On peut ici retirer le livre de la liste
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
        # On verifie que le numero de livre est valide
        livre = self.chercher_livre_numero(numero_livre)
        if livre == None:
            print('Emprunt impossible : livre inexistant')
            return None
            
        # On verifie qu'il reste des exemplaires disponibles pour ce livre
        if livre.get_nb_dispo() == 0:
            print('Emprunt impossible : plus d\'exemplaires disponibles')
            return None
            
        # On verifie que le numero de lecteur est valide
        lecteur = self.chercher_lecteur_numero(numero_lecteur)
        if lecteur == None:
            print('Emprunt impossible : lecteur inexistant')
            return None
        # On verifie que ce lecteur n'a pas deja emprunte ce livre
        e = self.chercher_emprunt(numero_lecteur, numero_livre)
        if e != None:
            print('Emprunt impossible : deja en cours')
            return None

        # Les conditions sont reunies pour pouvoir faire cet emprunt            
        self.__emprunts.append(Emprunt(numero_lecteur, numero_livre))
        livre.set_nb_dispo(livre.get_nb_dispo()-1)
        lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
        return self.__emprunts[-1]

    def retour_livre(self, numero_lecteur, numero_livre):
        # On recherche l'emprunt identifie par le numero de livre et de lecteur
        e = self.chercher_emprunt(numero_lecteur, numero_livre)
        if e != None: # l'emprunt existe, on le retire de la liste et on met a jour nb_emprunt pour le lecteur et nb_dispo pour le livre
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
           
