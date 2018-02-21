import turtle as t
import random as r
from pvector import PVector

class Particle(t.Turtle):
    
    def __init__(self, tshape, tcolor, x, y):
        t.Turtle.__init__(self)
        self.penup()
        self.shape(tshape)
        self.color(tcolor)
        self.speed = 1
        self.max_speed = 10
        self.location = PVector(x, y)
        self.setpos(self.location.x, self.location.y)
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(r.uniform(-1.0, 1.0), r.uniform(-2.0, 0.0))
        self.lifespan = 255
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= r.uniform(1.5, 3.0)
        if self.lifespan <= 0:
            self.lifespan = 0
        self.color((round(self.lifespan), 0, 0))
        self.setpos(self.location.x, self.location.y)
    
    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False
