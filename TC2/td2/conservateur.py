from personne import *

class Conservateur(Personne):
    def __init__(self, nom, prenom, adresse):
        Personne.__init__(self,nom,prenom,adresse)        
        