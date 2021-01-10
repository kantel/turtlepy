import turtle as t
import math

WIDTH = 640
HEIGHT = 480

palette = [(189, 183, 110), (0, 100, 0), (34, 139, 105),
           (152, 251, 152), (85, 107, 47), (139, 69, 19),
           (154, 205, 50), (107, 142, 35), (139, 134, 78),
           (139, 115, 85)]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor("#2b3e50")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Symmetrischer Pythagoras-Baum")

p = t.Turtle()
p.speed(0)
p.color(0, 0, 0)
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
    p.color(palette[int(s - 2)%10], palette[int(s - 2)%10])
    p.begin_fill()
    for _ in range(4):
        p.forward(s)
        p.right(90)
    p.end_fill()
        

p.penup()
p.setpos(-50, -HEIGHT/2 + 50)
# Bildschirm-Refresh ausschalten
wn.tracer(0)
p.pendown()
tree(100)
p.hideturtle()
# Bildschirm-Refresh wieder einschalten
wn.update()

print("I did it, Babe")

wn.mainloop()
