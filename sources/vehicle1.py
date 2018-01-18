# Random Walk mit Klassen

import turtle as t
import random as r
import math

WIDTH = 600
HEIGHT = 600

class Vehicle(t.Turtle):
    
    def __init__(self, tshape, tcolor, x, y):
        t.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(tshape)
        self.shapesize(stretch_wid = 0.6, stretch_len = 1.1, outline = None)
        self.color(tcolor)
        self.r = 3.0
        self.speed = 1
        self.max_speed = 4.0
        self.max_force = 0.1
        self.acceleration = t.Vec2D(0, 0)
        self.velocity = t.Vec2D(0, 0)
        self.location = t.Vec2D(x, y)
    
    def move(self):
        self.fd(self.speed)
    
    def update(self):
        self.velocity += self.acceleration
        # velocity.limit(maxspeed)
        self.location += self.velocity
        self.acceleration *= 0
    
    def apply_force(self, force):
        self.acceleration += force

wn = t.Screen()
wn.setup(WIDTH, HEIGHT)
wn.colormode(255)
wn.bgcolor(0, 0, 0)
wn.title("Vehicle (1)")

def exitWorld():
    global keepGoing
    keepGoing = False

vehicle = Vehicle("triangle", "red", 0, 0)

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(exitWorld, "Escape") # Escape beendet das Spiel

# Bildschirm-Refresh ausschalten
wn.tracer(0)

keepGoing = True
while keepGoing:
    wn.update()  # Den gesamten Bildschirm neuzeichnen
    vehicle.move()