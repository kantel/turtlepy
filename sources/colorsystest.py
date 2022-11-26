# Test des Colorsys-Moduls mit der Turtle
# Gleichzeitig Beispiel für die Portierung von TigerJython nach Python

import turtle as t
import colorsys

WIDTH = 600
HEIGHT = 600

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(54, 50, 80)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Colorsys-Test")

wn.colormode(1)
alice = t.Turtle()
alice.speed(0)
alice.pensize(3)

h = 0.0      # hue

for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)   # color
    alice.pencolor(c)
    h += 0.004
    alice.right(i)
    alice.circle(50, i)
    alice.forward(i)
    alice.left(91)


print("I did it, Babe")

wn.mainloop()
