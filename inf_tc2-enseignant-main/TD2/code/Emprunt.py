#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:27:13 2022

@author: dellandrea
"""

from datetime import date
from lecteur import *
from livre import *

# ***** classe Emprunt *****        
class Emprunt:
    def __init__(self,numero_lecteur,numero_livre):
        self.__numero_lecteur = numero_lecteur
        self.__numero_livre = numero_livre
        self.__date = date.isoformat(date.today())

    def get_numero_lecteur(self):
        return self.__numero_lecteur
        
    def get_numero_livre(self):
        return self.__numero_livre
        
    def get_date(self):
        return self.__date

    def __str__(self):
        return 'Emprunt - Numero lecteur : {}, Numero livre: {}, Date : {}'.format(self.__numero_lecteur,self.__numero_livre,self.__date)
  