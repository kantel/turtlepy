import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Hexagon-Schleife")

hexi = t.Turtle()
hexi.pensize(2)
hexi.pencolor(253, 141, 60)
hexa = t.Turtle()
hexa.pensize(2)
hexa.pencolor(240, 59, 32)

hexi.penup()
hexi.goto(75, 0)
hexi.pendown()

hexa.penup()
hexa.goto(-25, 0)
hexa.pendown()

for i in range(6):
    hexi.rt(60)
    hexi.fd(100)
    hexa.lt(60)
    hexa.fd(100)

wn.mainloop()