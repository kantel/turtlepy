# Asymmetrischer Pythagoras-Baum
# Wird als Postcript-File gespeichert und dann
# mittels PIL nach .jpg/.png konvertiert

import turtle as t
import math
from PIL import Image

WIDTH = 640  # 640
HEIGHT = 480 # 480
REC_LEVEL = 12      # Rekursions-Tiefe

palette = [(42, 40, 45), (160, 51, 46), (54, 50, 80),
           (50, 80, 105), (180, 144, 55),
           (215, 158, 40), (140, 82, 48)]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(230, 226, 204)
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
    p.color(palette[int(s)%len(palette)], palette[int(s)%len(palette)])
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
tree(85, REC_LEVEL) 
p.hideturtle()
# Bildschirm-Refresh wieder einschalten
wn.update()

file_name = "pythagoras"
cv = wn.getcanvas()
cv.postscript(file = file_name + ".eps", width = WIDTH, height = HEIGHT)
# p.getscreen().getcanvas().postscript(file = file_name + ".eps", width = WIDTH, height = HEIGHT)

img = Image.open(file_name + ".eps")
img.load(scale = 5)          # Bringt eine höhe Auflösung. Danke an Karsten W.
img.save(file_name + ".png")

print("I did it, Babe!")

wn.mainloop()
