# Random Walk auf einem orthogonalen Gitter

import turtle as t
import random as r
import math

wn = t.Screen()
wn.setup(width = 800, height = 800)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Random-Walk (1)")

SL = 3   # Schrittlänge

def random_walk(x, y):
    step = r.choice(["N", "S", "E", "W"])
    if step == "N":
        y += SL
    elif step == "S":
        y -= SL
    elif step == "E":
        x += SL
    elif step == "W":
        x -= SL
    else:
        print("Es ist was faul im Staate Dänemark")
    return(x, y)

def distance(a, b):
    return(math.sqrt(a**2 + b**2))/SL
 
colors = ["white", "yellow", "orange", "green", "blue", "purple", "red"]

alex = t.Turtle()
alex.speed(0)

x, y = 0, 0
for i in range(5000):
    if distance(x, y) < 10:
        color = 0
    elif distance(x, y) < 20:
        color = 1
    elif distance(x, y) < 30:
        color = 2
    elif distance(x, y) < 40:
        color = 3
    elif distance(x, y) < 50:
        color = 4
    elif distance(x, y) < 75:
        color = 5
    else:
        color = 6
    alex.pencolor(colors[color])
    alex.width(2)
    x, y = random_walk(x, y)
    alex.goto(x, y)
    
    if i > 100 and distance(x, y) < 2:
            print(i, distance(x, y))
    
print(distance(x, y))

wn.mainloop()