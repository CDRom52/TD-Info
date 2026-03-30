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

   
class Acteur(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.theatres = []
        self.costumes = []
        self.pieces_de_theatre = []
    
    def __str__(self):
        return f"Classe Acteur - nom : {self.nom}"

class Costumier(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.theatre = None
        self.costumes = []
    
    def __str__(self):
        return f"Classe Costumier - nom : {self.nom}"

class Metteur_en_scene(Personne):
    def __init__(self,nom):
        Personne.__init__(self, nom)
        self.theatres = []
        self.pieces_de_theatre = []
    
    def __str__(self):
        return f"Classe Metteur_en_scene - nom : {self.nom}"
        
class Piece_de_theatre:
    def __init__(self,nom):
        self.nom = nom
        self.theatres = []
        self.acteurs = []
        self.metteur_en_scene = None
    
    def __str__(self):
        return f"Classe Piece_de_theatre - nom : {self.nom}"   

class Costume:
    def __init__(self,nom):
        self.nom = nom
        self.theatre = None
        self.acteurs = []
        self.costumiers = []     
    
    def __str__(self):
        return f"Classe Costume - nom : {self.nom}"     
    
class Theatre:
    def __init__(self,nom):
        self.nom = nom
        self.metteurs_en_scene = []
        self.pieces_de_theatre = []
        self.acteurs = []
        self.costumiers = []        
        self.costumes = []
        
    def __str__(self):
        return f"Classe Theatre - nom : {self.nom}"     
    
if __name__ == '__main__':
    
    p = Personne("Marie")
    print(p)
    
    a = Acteur("Charles")
    print(a)
    
    c = Costumier("Paul")
    print(c)
    
    m = Metteur_en_scene("Delphine")
    print(m)
    
    pi = Piece_de_theatre("Hamlet")
    print(pi)
    
    co = Costume("Chique")
    print(co)
    
    t = Theatre("La Comédie Française")
    print(t)