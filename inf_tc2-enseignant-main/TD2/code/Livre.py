#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:26:54 2022

@author: dellandrea
"""

# ***** classe Livre *****          
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
