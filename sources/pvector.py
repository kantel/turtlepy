import math

class PVector():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# -- neu 21.01.18 -- #
    
    def set(self, v):
        self.x = v.x
        self.y = v.y
    
    def get(self):
        v = PVector(self.x, self.y)
        return v

# -- /neu 21.01.18 -- #
    
    def add(self, v):
        self.x += v.x
        self.y += v.y
        
    def sub(self, v):
        self.x -= v.x
        self.y -= v.y
    
    # Multiplikation mit einem Skalar
    def mult(self, n):
        self.x *= n
        self.y *= n
    
    # Division durch einen Skalar
    def div(self, n):
        self.x /= n
        self.y /= n

# -- neu 21.01.18 -- #

    # Elementweise Multiplikation eines Vektor mit einem anderen Vektor
    def mult2(self, v):
        self.x *= v.x
        self.y *= v.y

    # Elementweise Division eines Vektor mit einem anderen Vektor
    def div2(self, v):
        self.x /= v.x
        self.y /= v.y

# -- /neu 21.01.18 -- #

    # Magnitude (Betrag/Länge) eines Vektors
    def mag(self):
        return (math.sqrt(self.x*self.x + self.y*self.y))
    
    # Normalisierung
    def normalize(self):
        m = self.mag()
        if (m != 0):
            self.div(m)

# -- neu 21.01.18 -- #

    # Berechnung der euklidischen Distanz zwischen zwei Vektoren
    def dist(self, v):
        dx = self.x - v.x
        dy = self.y - v.y
        return (math.sqrt(dx*dx + dy+dy))
    
    # Berechnung des Skalarprodukts (inneren Produkts) eines Vektors
    def dot(self, v):
        return self.x*v.x + self.y*v.y
    
    # Begrenzt die Magnitude eines Vektors auf max
    def limit(self, max):
        if self.mag() > max:
            self.normalize()
            self.mult(max)
    
    # Berechnet den Winkel der Rotation eines Vektors
    def heading(self):
        angle = math.atan2(-self.y, self.x)
        return -1*angle

# -- /neu 21.01.18 -- #
