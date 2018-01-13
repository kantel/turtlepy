# Random Walk mit Klassen

import turtle as t
import random as r
import math


WIDTH = 800
HEIGHT = 800

class RandomWalker(t.Turtle):
    
    def __init__(self, tcolor, levi = True):
        t.Turtle.__init__(self)
        self.pencolor(tcolor)
        self.hideturtle()
        self.levi = levi
        self.speed(0)
        self.speed = 1
        self.pendown()
        self.start_x = 0
        self.start_y = 0
        self.goto(self.start_x, self.start_y)
    
    def calc_next(self):
        if self.levi:
            self.x_dist = r.choice([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 10])
            self.y_dist = r.choice([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 10])
        else:
            self.x_dist = r.choice([0, 1, 2, 3, 4])
            self.y_dist = r.choice([0, 1, 2, 3, 4])
        
        self.x_dir = r.choice([-1, 1])
        self.y_dir = r.choice([-1, 1])
        self.new_x = self.x_dist*self.x_dir
        self.new_y = self.y_dist*self.y_dir

    def move(self):
        self.goto(self.start_x + self.new_x, self.start_y + self.new_y)
        self.start_x += self.new_x
        if self.start_x > WIDTH/2 - 40:
            self.start_x = WIDTH/2 - 40
        elif self.start_x < -WIDTH/2 + 40:
            self.start_x = -WIDTH/2 + 40
        self.start_y += self.new_y
        if self.start_y > HEIGHT/2 - 40:
            self.start_y = HEIGHT/2 - 40
        elif self.start_y < -HEIGHT/2 + 40:
            self.start_y = -HEIGHT/2 + 40
        
wn = t.Screen()
wn.setup(WIDTH, HEIGHT)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Random-Walk (4)")

# Bildschirm-Refresh ausschalten
wn.tracer(0)

colors = ["white", "yellow", "orange", "green", "dodger blue", "purple", "red"]
walkers = []
for i in range(len(colors)):
    walker = RandomWalker(colors[i])
    walkers.append(walker)

for i in range(5000):
    for i in range(len(colors)):
        walkers[i].calc_next()
        # Ignoriere Schritte, die nirgendwohin führen
        if walkers[i].new_x == 0 and walkers[i].new_y == 0:
            continue
        walkers[i].move()
    wn.update()
    

print("I did it, Babe!")
    
wn.mainloop()