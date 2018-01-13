# Random Walk mit beliebigem Winkel

import turtle as t
import random as r
import math

wn = t.Screen()
wn.setup(width = 800, height = 800)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Random-Walk (2)")

SL = 3   # Schrittlänge

def distance(a, b):
    return(math.sqrt(a**2 + b**2))/SL
 
colors = ["white", "yellow", "orange", "green", "blue", "purple", "red"]

alex = t.Turtle()
alex.speed(0)

x, y = 0, 0
for i in range(5000):
    if distance(alex.xcor(), alex.ycor()) < 10:
        color = 0
    elif distance(alex.xcor(), alex.ycor()) < 20:
        color = 1
    elif distance(alex.xcor(), alex.ycor()) < 30:
        color = 2
    elif distance(alex.xcor(), alex.ycor()) < 40:
        color = 3
    elif distance(alex.xcor(), alex.ycor()) < 50:
        color = 4
    elif distance(alex.xcor(), alex.ycor()) < 75:
        color = 5
    else:
        color = 6
    alex.pencolor(colors[color])
    alex.width(2)
    alex.right(r.randint(1, 360))
    alex.fd(SL)
    
    if i > 100 and distance(alex.xcor(), alex.ycor()) < 2:
        print(i, distance(alex.xcor(), alex.ycor()))

print(i, distance(alex.xcor(), alex.ycor()))

wn.mainloop()