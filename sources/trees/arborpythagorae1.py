# Symmetrischer Pythagorasbaum
import turtle as t
import math

WIDTH, HEIGHT = 640, 400

palette = [(42, 40, 45), (54, 50, 80), (160, 51, 46),
           (50, 80, 105), (215, 158, 40),
           (180, 144, 55), (140, 82, 48)]

wn = t.Screen()
wn.setup(width = WIDTH, height = HEIGHT, startx = 2000, starty = 80)
wn.colormode(255)
wn.title("Arbor Pythagorae 1")
wn.bgcolor(230, 226, 204)

p = t.Turtle()
p.speed(0)
p.pencolor(0, 100, 0)   # Dunkles Grün
p.setheading(90)

def tree(s):
    if s < 2:
        return
    quadrat(s)
    p.forward(s)
    s1 = s/math.sqrt(2)
    p.left(45)
    tree(s1)
    p.right(90)
    p.forward(s1)
    tree(s1)
    p.back(s1)
    p.left(45)
    p.back(s)

def quadrat(s):
    p.fillcolor(palette[int(s%len(palette) - 1)])
    p.begin_fill()
    for _ in range(4):
        p.forward(s)
        p.right(90)
    p.end_fill()

p.penup()
p.setpos(-50, -HEIGHT/2 + 20)
# Bildschirm-Refresh ausschalten
wn.tracer(0)
p.pendown()
tree(90)
p.hideturtle()
# Bildschirm-Refresh wieder einschalten
wn.update()

print("I did it, Babe!")

wn.mainloop()