import turtle as t
import random as r

WIDTH = 600
HEIGHT = 600

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Creatures 01")

def walk(d):
    x = r.randint(-d, d)
    y = r.randint(-d, d)
    # print(x, y)
    return(x, y)

def exitWorld():
    global keepGoing
    print("I did it, Babe!")
    keepGoing = False

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(exitWorld, "Escape") # Escape beendet das Spiel

# Bildschirm-Refresh ausschalten
wn.tracer(0)

ants1 = []
ants2 = []

for i in range(25):
    ants1.append(t.Turtle())
    ants1[i].shape("circle")
    ants1[i].color("red")
    ants1[i].penup()
    ants1[i].shapesize(stretch_wid = 0.2, stretch_len = 0.2, outline = None)
    # ants1[i].setpos(r.randint(-WIDTH/2, WIDTH/2), r.randint(-HEIGHT/2, HEIGHT/2))

for i in range(5):
    ants2.append(t.Turtle())
    ants2[i].shape("circle")
    ants2[i].color("green")
    ants2[i].penup()
    ants2[i].shapesize(stretch_wid = 0.5, stretch_len = 0.5, outline = None)
    # ants2[i].setpos(r.randint(-WIDTH/2, WIDTH/2), r.randint(-HEIGHT/2, HEIGHT/2))

x, y = 0, 0
keepGoing = True
while keepGoing:
    wn.update()
    for i in range(len(ants1)):
        a, b = walk(6)
        ants1[i].setpos(ants1[i].xcor() + a, ants1[i].ycor() + b)
        # Ränder überprüfen
        if ants1[i].xcor() < -WIDTH/2:
            ants1[i].setx(WIDTH/2)
        if ants1[i].xcor() > WIDTH/2:
            ants1[i].setx(-WIDTH/2)
        if ants1[i].ycor() < -WIDTH/2:
            ants1[i].sety(WIDTH/2)
        if ants1[i].ycor() > WIDTH/2:
            ants1[i].sety(-WIDTH/2)
    for i in range(len(ants2)):
        a, b = walk(2)
        ants2[i].setpos(ants2[i].xcor() + a, ants2[i].ycor() + b)
        # Ränder überprüfen
        if ants2[i].xcor() < -WIDTH/2:
            ants2[i].setx(WIDTH/2)
        if ants2[i].xcor() > WIDTH/2:
            ants2[i].setx(-WIDTH/2)
        if ants2[i].ycor() < -WIDTH/2:
            ants2[i].sety(WIDTH/2)
        if ants2[i].ycor() > WIDTH/2:
            ants2[i].sety(-WIDTH/2)

