#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:21:29 2022

@author: dellandrea
"""

from lecteur import *

l = Lecteur("Durand","Marie","Ecully",13)

print(l)

l.set_nom("Dupond")
print(l.get_nom())

    
l.set_prenom("Emilie")
print(l.get_prenom())
    
l.set_adresse("Lyon")
print(l.get_adresse())   

l.set_numero(14)
print(l.get_numero())
        
l.set_nb_emprunts(2)
print(l.get_nb_emprunts())

print(l)