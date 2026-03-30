from personne import *

class Lecteur(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse)        
        self.__numero = numero
        self.__nb_emprunts = 0
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
        
    def set_nb_emprunts(self,nb_emprunts):
        self.__nb_emprunts = nb_emprunts
        
    def get_nb_emprunts(self):
        return self.__nb_emprunts
        
    def __str__(self):
        return 'Lecteur - Nom : {}, Prenom : {}, Adresse : {}, Numero : {}, Nb emprunts : {}'.format(self.get_nom(),self.get_prenom(),self.get_adresse(),self.__numero,self.__nb_emprunts)