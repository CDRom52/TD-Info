#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:21:29 2022

@author: dellandrea
"""

from personne import *

p = Personne("Durand","Marie","Ecully")

print(p)

p.set_nom("Dupond")
print(p.get_nom())

    
p.set_prenom("Emilie")
print(p.get_prenom())
    
p.set_adresse("Lyon")
print(p.get_adresse())    

print(p)