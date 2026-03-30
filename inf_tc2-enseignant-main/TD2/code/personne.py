#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:21:05 2022

@author: dellandrea
"""

# ***** classe Personne *****
class Personne:
    def __init__(self,nom,prenom,adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        
    def __str__(self):
        return f"Classe Personne - Nom : {self.__nom}, Prenom : {self.__prenom}, Adresse : {self.__adresse}"
        
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