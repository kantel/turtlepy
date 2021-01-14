import turtle as t
import math

WIDTH = 640
HEIGHT = 480

palette = [(189, 183, 110), (34, 139, 105), (154, 205, 50),
           (139, 115, 85), (85, 107, 47), (139, 69, 19),
           (107, 142, 35), (139, 134, 78), (152, 251, 152),
           (0, 100, 0)]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor("#2b3e50")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Asymmetrischer Pythagoras-Baum")

p = t.Turtle()
p.speed(0)
p.color(0, 100, 0)
p.setheading(90)

def tree(s, level):
    if level < 1:
        return
    else:
        quadrat(s)
        # Linke Seite
        ls = s*math.sqrt(3)/2
        p.forward(s)
        p.left(90)
        p.forward(s)
        p.right(150)
        p.forward(ls)
        p.left(90)
        tree(ls, level - 1)
        # Rechte Seite
        rs = s/2
        p.right(180)
        p.forward(rs)
        p.left(90)
        tree(rs, level - 1)
        p.left(60)
        p.back(s)

def quadrat(s):
    p.color(palette[int(s - 2)%10], palette[int(s - 2)%10])
    p.begin_fill()
    for _ in range(4):
        p.forward(s)
        p.left(90)
    p.end_fill()

p.penup()
p.setpos(120, -HEIGHT/2 + 60)
# Bildschirm-Refresh ausschalten
wn.tracer(0)
p.pendown()
# Für eine Rekursionstiefe > 14 braucht man schon sehr viel Geduld
tree(85, 14) 
p.hideturtle()
print("I did it, Babe")
# Bildschirm-Refresh wieder einschalten
wn.update()

wn.mainloop()
