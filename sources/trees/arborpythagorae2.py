# Asymmetrischer Pythagorasbaum
import turtle as t
import math

WIDTH, HEIGHT = 640, 400
REC_LEVEL = 12   # Rekursionstiefe

palette = [(42, 40, 45), (54, 50, 80), (160, 51, 46),
           (50, 80, 105), (215, 158, 40),
           (180, 144, 55), (140, 82, 48)]

wn = t.Screen()
wn.setup(width = WIDTH, height = HEIGHT, startx = 2000, starty = 80)
wn.colormode(255)
wn.title("Arbor Pythagorae 2")
wn.bgcolor(230, 226, 204)

p = t.Turtle()
p.speed(0)
p.pencolor(0, 100, 0)   # Dunkles Grün
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
    p.fillcolor(palette[int(s%len(palette) - 1)])
    p.begin_fill()
    for _ in range(4):
        p.forward(s)
        p.left(90)
    p.end_fill()

p.penup()
p.setpos(120, -HEIGHT/2 + 30)
# Bildschirm-Refresh ausschalten
wn.tracer(0)
p.pendown()
# Für eine Rekursionstiefe > 14 braucht man schon sehr viel Geduld
tree(80, REC_LEVEL)
p.hideturtle()
# Bildschirm-Refresh wieder einschalten
wn.update()

print("I did it, Babe!")

wn.mainloop()