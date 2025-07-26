import turtle
from random import randint

WIDTH, HEIGHT = 640, 400

wn = turtle.Screen()
wn.setup(width=WIDTH, height=HEIGHT, startx = 2000, starty = 80)
wn.setworldcoordinates(0, 0, WIDTH, HEIGHT)
wn.title("Fractal Tree 2")
wn.colormode(255)
wn.bgcolor(210, 219, 142)
wn.tracer(0)

alice = turtle.Turtle()
alice.speed(0)
alice.hideturtle()

def draw_branch(start_position, direction, branch_length):
    if branch_length < 2:
        return

    # Startposition und initiale Richtung
    alice.penup()
    alice.goto(start_position)
    alice.setheading(direction)

    # Zeichne einen Zweig
    alice.pendown()
    # Die Dicke des Zweiges beträgt 1/7 der Zweiglänge, aber mindestens 1
    alice.pensize(max(branch_length / 7.0, 1))
    # Farben in Abängigkeit von der Dicke des Stammes
    if branch_length >= 70:
        alice.pencolor(139, 69, 19)
    elif branch_length >= 65:
        alice.pencolor(139, 115, 85)
    elif branch_length >= 60:
        alice.pencolor(139, 134, 78)
    elif branch_length >= 55:
        alice.pencolor(189, 183, 110)
    elif branch_length >= 40:
        alice.pencolor(85, 107, 47)
    elif branch_length >= 25:
        alice.pencolor(107, 142, 35)
    else:
        alice.pencolor(0, 100, 0)

    alice.forward(branch_length)

    # Spechere die Position am Ende des Zweiges
    end_position = alice.position()
    left_direction = direction + randint(10, 30)
    left_branch_length = branch_length - randint(8, 15)
    right_direction = direction - randint(10, 30)
    right_branch_length = branch_length - randint(8, 15)

    # Rekursion
    draw_branch(end_position, left_direction, left_branch_length)
    draw_branch(end_position, right_direction, right_branch_length)


# (Pseudo-) Zufallswert für die Startlänge des Stamms
start_length = randint(60, 90)

# Zeichne den Baum
draw_branch((WIDTH // 2, 10), 90, start_length)
wn.update()

print("I did it, Babe!")
wn.mainloop()