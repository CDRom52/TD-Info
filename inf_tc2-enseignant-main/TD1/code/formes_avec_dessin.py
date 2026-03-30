class Forme:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
        self.__dessins = []
    
    def get_pos(self):
        return self.__x, self.__y
    
    def set_pos(self, x, y):
        self.__x = x
        self.__y = y
    
    def translation(self, dx, dy):
        self.__x += dx
        self.__y += dy
        
    def add_dessin(self,d):
        self.__dessins.append(d)
    
    def del_dessin(self,d):
        self.__dessins.remove(d)

    def print_dessins(self):
        print("Liste des dessins de la forme : ")
        for d in self.__dessins:
            print(d.get_nom())

class Rectangle(Forme):
    def __init__(self, x, y, l, h):
        Forme.__init__(self, x, y)
        self.__l = l
        self.__h = h
    
    def __str__(self):
        return f"Rectangle d'origine {self.get_pos()} et de dimensions {self.__l}x{self.__h}"
    
    def get_dim(self):
        return self.__l, self.__h
    
    def set_dim(self, l, h):
        self.__l = l
        self.__h = h
    
    def contient_point(self, x, y):
        X, Y = self.get_pos()
        return X <= x <= X + self.__l and \
               Y <= y <= Y + self.__h
    
    def redimension_par_points(self, x0, y0, x1, y1):
        self.set_pos(min(x0, x1), min(y0, y1))
        self.__l = abs(x0 - x1)
        self.__h = abs(y0 - y1)

class Ellipse(Forme):
    def __init__(self, x, y, rx, ry):
        Forme.__init__(self, x, y)
        self.__rx = rx
        self.__ry = ry
    
    def __str__(self):
        return f"Ellipse de centre {self.get_pos()} et de rayons {self.__rx}x{self.__ry}"
    
    def get_dim(self):
        return self.__rx, self.__ry
    
    def set_dim(self, rx, ry):
        self.__rx = rx
        self.__ry = ry
    
    def contient_point(self, x, y):
        X, Y = self.get_pos()
        return ((x - X) / self.__rx) ** 2 + ((y - Y) / self.__ry) ** 2 <= 1
    
    def redimension_par_points(self, x0, y0, x1, y1):
        self.set_pos((x0 + x1) // 2, (y0 + y1) // 2)
        self.__rx = abs(x0 - x1) / 2
        self.__ry = abs(y0 - y1) / 2

class Cercle(Ellipse):
    def __init__(self, x, y, r):
        Ellipse.__init__(self, x, y, r, r)
    
    def __str__(self):
        return f"Cercle de centre {self.get_pos()} et de rayon {self.get_dim()}"
    
    def get_dim(self):
        return Ellipse.get_dim(self)[0]
    
    def set_dim(self, r):
        Ellipse.set_dim(self, r, r)
    
    def redimension_par_points(self, x0, y0, x1, y1):
        r = min(abs(x0 - x1), abs(y0 - y1)) / 2
        self.set_dim(r)
        self.set_pos(round(x0 + r if x1 > x0 else x0 - r),
                     round(y0 + r if y1 > y0 else y0 - r))

class Dessin:
    def __init__(self,n):
        self.__nom = n
        self.__formes = []

    def get_nom(self):
        return self.__nom

    def add_forme(self,f):
        self.__formes.append(f)
        f.add_dessin(self)
        
    def del_forme(self,position):
        f = self.__formes.pop(position)
        f.del_dessin(self)

    def print_formes(self):
        print('--- Dessin ---')
        for f in self.__formes:
            print(f)

    def __str__(self):
        s = '--- Dessin (avec print) ---'
        for f in self.__formes:
            s += '\n' + str(f)
        return s