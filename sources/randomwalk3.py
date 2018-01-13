# Random Walk mit beliebigem Winkel und variabler Schrittlänge

import turtle as t
import random as r
import math

WIDTH = 800
HEIGHT = 800

wn = t.Screen()
wn.setup(WIDTH, HEIGHT)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Random-Walk (3)")


def distance(a, b):
    return(math.sqrt(a**2 + b**2))   #/SL
 
colors = ["white", "yellow", "orange", "green", "dodger blue", "purple", "red"]

alex = t.Turtle()
alex.speed(0)
alex.pendown()
alex.goto(0, 0)

start_x, start_y = 0, 0
for i in range(5000):
    if distance(alex.xcor(), alex.ycor()) < 50:
        color = 0
    elif distance(alex.xcor(), alex.ycor()) < 100:
        color = 1
    elif distance(alex.xcor(), alex.ycor()) < 150:
        color = 2
    elif distance(alex.xcor(), alex.ycor()) < 200:
        color = 3
    elif distance(alex.xcor(), alex.ycor()) < 250:
        color = 4
    elif distance(alex.xcor(), alex.ycor()) < 300:
        color = 5
    else:
        color = 6
    alex.pencolor(colors[color])
    
    x_dir = r.choice([-1, 1])
    # ohne Lévy-Fly
    # x_dist = r.choice([0, 1, 2, 3])
    # mit Lévy-Fly
    x_dist = r.choice([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 10])
    new_x = x_dist*x_dir
    
    y_dir = r.choice([-1, 1])
    # ohne Lévy-Fly
    # y_dist = r.choice([0, 1, 2, 3])
    # mit Lévy-Fly
    y_dist = r.choice([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 10])
    new_y = y_dist*y_dir
    
    # Ignoriere Schritte, die nirgendwohin führen
    if new_x == 0 and new_y == 0:
        continue
    
    alex.goto(start_x + new_x, start_y + new_y)
    start_x += new_x
    if start_x > WIDTH/2:
        start_x = WIDTH/2
    elif start_x < -WIDTH/2:
        start_x = -WIDTH/2
    start_y += new_y
    if start_y > HEIGHT/2:
        start_y = HEIGHT/2
    elif start_y < -HEIGHT/2:
        start_y = -HEIGHT/2
    

print("I did it, Babe!")
    
wn.mainloop()