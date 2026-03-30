#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:05:14 2022

@author: dellandrea
"""

class Personne:
    def __init__(self,nom):
        self.nom  = nom
        
    def __str__(self):
        return f"Classe Personne - nom : {self.nom}"

   
class Client(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.hotels = []
        self.chambres = []
    
    def __str__(self):
        return f"Classe Client - nom : {self.nom}"

class Directeur(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.hotels = []
    
    def __str__(self):
        return f"Classe Directeur - nom : {self.nom}"

class Television:
    def __init__(self,nom):
        self.nom  = nom
        self.chambre = None
        
    def __str__(self):
        return f"Classe Television - nom : {self.nom}"

class Lit:
    def __init__(self,nom):
        self.nom  = nom
        self.chambre = None
        
    def __str__(self):
        return f"Classe Lit - nom : {self.nom}"

class Salle_de_bain:
    def __init__(self,nom):
        self.nom  = nom
        self.chambre = None
        
    def __str__(self):
        return f"Classe Salle_de_bain - nom : {self.nom}"     
    
class Chambre:
    def __init__(self,nom,hotel,nom_tele,nom_lit,nom_sdb):
        self.nom  = nom
        self.hotel = hotel
        self.clients = []
        self.television = Television(nom_tele)
        self.lit = Lit(nom_lit)
        self.salle_de_bain = Salle_de_bain(nom_sdb)
        
    def __str__(self):
        return f"Classe Chambre - nom : {self.nom}"
     
    
class Hotel:
    def __init__(self,nom):
        self.nom = nom
        self.directeur = None
        self.clients = []
        self.chambres = []        
    
    def __str__(self):
        return f"Classe Hotel - nom : {self.nom}"     
    
if __name__ == '__main__':
    
    p = Personne("Marie")
    print(p)
    
    cl = Client("Charles")
    print(cl)
    
    d = Directeur("Maxime")
    print(d)
    
    h = Hotel("L'Europeen")
    print(h)
    
    sdb = Salle_de_bain("Ocean")
    print(sdb)
    
    t = Television("Tashibo")
    print(t)
    
    l = Lit("Confort")
    print(l)
    
    ch = Chambre("101",h,"Samsing","Relax","Plage")
    print(ch)