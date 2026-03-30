from formes_avec_dessin import *

def test_Rectangle():
    r = Rectangle(10, 20, 100, 50)
    str(r)
    assert r.contient_point(50, 50)
    assert not r.contient_point(0, 0)
    r.redimension_par_points(100, 200, 1100, 700)
    assert r.contient_point(500, 500)
    assert not r.contient_point(50, 50)

def test_Ellipse():
    e = Ellipse(60, 45, 50, 25)
    str(e)
    assert e.contient_point(50, 50)
    assert not e.contient_point(11, 21)
    e.redimension_par_points(100, 200, 1100, 700)
    assert e.contient_point(500, 500)
    assert not e.contient_point(101, 201)

def test_Cercle():
    c = Cercle(10, 20, 30)
    str(c)
    assert c.contient_point(0, 0)
    assert not c.contient_point(-19, -9)
    c.redimension_par_points(100, 200, 1100, 700)
    assert c.contient_point(500, 500)
    assert not c.contient_point(599, 500)
    
def test_Dessin():
    # Partie pour aller plus loin : Creation et manipulation d'objets Dessin
    
    r = Rectangle(10, 20, 100, 50)
    e = Ellipse(60, 45, 50, 25)
    c = Cercle(10, 20, 30)
    
    print("Création d'un dessin A composé des trois formes")
    d1 = Dessin("A")
    d1.add_forme(r)
    d1.add_forme(e)
    d1.add_forme(c)
    d1.print_formes()

    print("Création d'un dessin B composé de l'ellipse et du cercle")
    d2 = Dessin("B")
    d2.add_forme(e)
    d2.add_forme(c)
    d2.print_formes()

    print("Affichage des dessins auxquels les formes sont associées")
    r.print_dessins()
    e.print_dessins()
    c.print_dessins()

    print("Suppression de l'ellipse dans le dessin A")
    d1.del_forme(1)
    print(d1)

    print("Affichage des dessins auxquels les formes sont associées")
    r.print_dessins()
    e.print_dessins()
    c.print_dessins()

if __name__ == '__main__':
    test_Rectangle()
    test_Ellipse()
    test_Cercle()
    test_Dessin()
