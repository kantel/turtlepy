# Die Kochsche Schneeflocke mit der Turtlegraphik

import turtle as t

colors = [(150, 100, 255), (255, 100, 150), (150, 255, 100), (255, 150, 100)]
seiten = 4      # Anzahl der Seiten der Schneeflocke, entweder 3 odeer 4
it = 4          # Iterationstiefe, entweder 3 oder 4

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.setup(width = 400, height = 400)
wn.title("Kochsche Schneeflocke")

def kochkurve(length, d):
    if d == 0:
        koch.forward(length)
    else:
        kochkurve(length/3, d-1)
        koch.left(60)
        kochkurve(length/3, d-1)
        koch.right(120)
        kochkurve(length/3, d-1)
        koch.left(60)
        kochkurve(length/3, d-1)


def schneeflocke(length, d):
    for i in range(seiten):
        koch.pencolor(colors[i % 4])
        kochkurve(length, d)
        koch.right(360/seiten)

koch = t.Turtle()
koch.pensize(1)
koch.penup()
koch.speed(0)
koch.goto(-100, 100)
koch.pendown()
schneeflocke(200, it)

wn.mainloop()