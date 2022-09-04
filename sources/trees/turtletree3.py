# Fraktaler Baum (mit der Turtle gezeichnet)
# Nach Al Sweigart »The Recursive Book of Recursion«, Seite 187ff
# Modifiziert von -ka-

import random, time
import turtle as t

WIDTH = 600
HEIGHT = 600

# Initialisierung der Turtle
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(235, 215, 182)
wn.setup(width = WIDTH, height = HEIGHT)
wn.setworldcoordinates(0, 0, WIDTH, HEIGHT)
wn.title("Fraktaler Baum nach Al Sweigart")

alice = t.Turtle()
alice.speed(0)        # Höchstgeschwindigkeit
# alice.hideturtle()

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
    alice.forward(branch_length)
    
    # Speichere die Position am Ende des Zweigs
    end_position = alice.position()
    left_direction = direction + left_angle
    left_branch_length = branch_length - left_decrease
    rigth_direction = direction - rigth_angle
    right_branch_length = branch_length - right_decrease
    
    # Rekursion
    draw_branch(end_position, left_direction, left_branch_length)
    draw_branch(end_position, right_direction, right_branch_length)
    
    # Hauptprogramm
    seed = 250
    while True:
        # (Pseudo-) Zufallswerte für die Eigenschaften der Zweige
        random.seed(seed)
        left_angle     = random.randint(10,  30)
        left_decrease  = random.randint( 8,  15)
        rigth_angle    = random.randint(10,  30)
        right_decrease = random.randint( 8,  15)
        start_length   = random.randint(80, 120)
        
        # Ausgabe der Seed-Nummer
        alice.clear()
        alice.penup()
        alice.goto(10, 10)
        print(seed)
        alice.write("Seed: %s" % (seed))

# wn.mainloop()