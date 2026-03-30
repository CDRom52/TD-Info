from tkinter import *
from formes import *
from tkinter.colorchooser import askcolor

class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="grey")
        # self.title('Tirage aléatoire')
        # self.geometry('300x100+400+400')
        self.formes = []
        self.forme = None
        self.couleur = "white"
        self.forme_selectionnee = None
        self.x0, self.y0 = 0, 0

        self.canvas = ZoneAffichage(self, 500, 200)
        self.canvas.pack(side =BOTTOM, padx=5, pady=5)

        boutonRectangle = Button(self, text='Rectangle')
        boutonRectangle.pack(side=LEFT, padx=5, pady=5)
        boutonEllipse = Button(self, text='Ellipse')
        boutonEllipse.pack(side=LEFT, padx=5, pady=5)
        boutonCouleur = Button(self, text='Couleur')
        boutonCouleur.pack(side=LEFT, padx=5, pady=5)
        boutonExporter = Button(self, text='Exporter')
        boutonExporter.pack(side=LEFT, padx=5, pady=5)
        boutonQuitter = Button(self, text='Quitter')
        boutonQuitter.pack(side=LEFT, padx=5, pady=5)

        boutonQuitter.config(command=self.destroy)
        boutonRectangle.config(command=self.rectangle)
        boutonEllipse.config(command=self.ellipse)
        boutonCouleur.config(command=self.choix_couleur)
        boutonExporter.config(command=self.exporter_svg)
        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.bouton_appuye)
        self.canvas.bind("<B1-Motion>", self.mouvement_souris)
        self.canvas.bind("<ButtonRelease-1>", self.bouton_relache)
        self.canvas.bind("<Control-ButtonRelease-1>", self.control_click)

    def exporter_svg(self):
        nom_fichier = "mon_dessin.svg"
        with open(nom_fichier, "w") as f:
            f.write('<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">\n')
            for forme in self.formes:
                f.write("  " + forme.vers_svg() + "\n")
            f.write('</svg>')
        print(f"Exporté dans {nom_fichier}")

    def rectangle(self):
        self.forme = "rectangle"

    def ellipse(self):
        self.forme = "ellipse"

    def choix_couleur(self):
        self.couleur = askcolor()
        if self.couleur[1]:
            self.couleur = self.couleur[1]

    def control_click(self, event):
        x, y = event.x, event.y
        for forme in reversed(self.formes):
            if forme.contient_point(x, y):
                forme.effacer()
                self.formes.remove(forme)
                break

    def bouton_appuye(self, event):
        self.x0, self.y0 = event.x, event.y
        self.forme_selectionnee = None
        for forme in reversed(self.formes):
            if forme.contient_point(event.x, event.y):
                self.forme_selectionnee = forme
                break
            
        if not self.forme_selectionnee:    
            if self.forme == "rectangle":
                new_f = Rectangle(self.canvas, event.x, event.y, 0, 0, self.couleur)
                self.formes.append(new_f)
                self.forme_selectionnee = new_f
            elif self.forme == "ellipse":
                new_f = Ellipse(self.canvas, event.x, event.y, 0, 0, self.couleur)
                self.formes.append(new_f)
                self.forme_selectionnee = new_f

    def mouvement_souris(self, event):
        if self.forme_selectionnee:
            print(self.forme_selectionnee)
            self.forme_selectionnee.redimension_par_points(self.x0, self.y0, event.x, event.y)

    def bouton_relache(self, event):
        self.forme_selectionnee = None
        
if __name__ == "__main__":
    fen = FenPrincipale()
    fen.mainloop()