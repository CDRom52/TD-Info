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
        self.restaurants = []
        self.plats = []
    
    def __str__(self):
        return f"Classe Client - nom : {self.nom}"

class Serveur(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.restaurant = None
        self.plats = []
    
    def __str__(self):
        return f"Classe Serveur - nom : {self.nom}"

class Directeur(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.restaurants = []
    
    def __str__(self):
        return f"Classe Directeur - nom : {self.nom}"
    
class Cuisinier(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.restaurant = None
        self.plats = []
    
    def __str__(self):
        return f"Classe Cuisinier - nom : {self.nom}"
    
    
class Plat:
    def __init__(self,nom):
        self.nom = nom
        self.restaurants = []
        self.cuisiniers = []
        self.serveurs = []
        self.clients = []
    
    def __str__(self):
        return f"Classe Plat - nom : {self.nom}"   
    
class Restaurant:
    def __init__(self,nom):
        self.nom = nom
        self.directeur = None
        self.cuisiniers = []
        self.serveurs = []
        self.clients = []
        self.plats = []        
    
    def __str__(self):
        return f"Classe Restaurant - nom : {self.nom}"     
    
if __name__ == '__main__':
    
    p = Personne("Marie")
    print(p)
    
    cl = Client("Charles")
    print(cl)
    
    s = Serveur("Paul")
    print(s)
    
    d = Directeur("Maxime")
    print(d)
    
    cu = Cuisinier("Sabine")
    print(cu)
    
    p = Plat("Lasagnes")
    print(p)
    
    r = Restaurant("Chez Lulu")
    print(r)