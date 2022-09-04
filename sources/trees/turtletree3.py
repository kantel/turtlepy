# Fraktaler Baum (mit der Turtle gezeichnet)
# Nach Al Sweigart »The Recursive Book of Recursion«, Seite 187ff
# Modifiziert von -ka-

import random, time
import turtle as t

WIDTH = 650
HEIGHT = 550

# Initialisierung der Turtle
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(235, 215, 182)  # Packpapier
wn.setup(width = WIDTH, height = HEIGHT, startx = 1400, starty = 50)
wn.setworldcoordinates(0, 0, WIDTH, HEIGHT)
wn.title("Fraktaler Baum nach Al Sweigart")
wn.tracer(0)

alice = t.Turtle()
alice.speed(0)        # Höchstgeschwindigkeit
alice.hideturtle()

def draw_branch(start_position, direction, branch_length):
    if branch_length < 3:
        # base case
        return()
    
    # Startposition und initiale Richtung
    alice.penup()
    alice.goto(start_position)
    alice.setheading(direction)
    
    # Zeichne einen Zweig
    alice.pendown()
    # Zweigdicke ist 1/7 der Zweiglänge
    alice.pensize(max(branch_length/7.0, 1))
    if alice.pensize() >= 9.5:
        alice.pencolor(139, 69, 19)
    elif alice.pensize() >= 8.5:
        alice.pencolor(139, 115, 85)
    elif alice.pensize() >= 7.0:
        alice.pencolor(139, 134, 78)
    elif alice.pensize() >= 5.5:
        alice.pencolor(189, 183, 110)
    elif alice.pensize() >= 4.0:
        alice.pencolor(85, 107, 47)
    elif alice.pensize() >= 2.5:
        alice.pencolor(107, 142, 35)
    else:
        alice.pencolor(0, 100, 0)
    alice.forward(branch_length)
    
    # Speichere die Position am Ende des Zweigs
    end_position = alice.position()
    left_direction = direction + random.randint(10, 30)
    left_branch_length = branch_length - random.randint(8, 15)
    right_direction = direction - random.randint(10, 30)
    right_branch_length = branch_length - random.randint(8, 15)
    
    # Rekursion
    draw_branch(end_position, left_direction, left_branch_length)
    draw_branch(end_position, right_direction, right_branch_length)
    
# Hauptprogramm
iteration = 0
while True:
    # (Pseudo-) Zufallswert für die Startlänge des Stamms
    start_length   = random.randint(85, 100)
    
    # Ausgabe der Seed-Nummer
    alice.clear()
    alice.penup()
    alice.goto(10, 10)
    alice.pencolor(45, 45, 45)
    alice.write("Iteration No.: %s" % (iteration))
    
    # Zeichne den Baum
    draw_branch((WIDTH//2, 10), 90, start_length)
    wn.update()
    time.sleep(2)
    
    iteration += 1
