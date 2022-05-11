import turtle as t

wn = t.Screen()
wn.bgcolor("#e6e2cc")
wn.setup(width = 640, height = 400)
wn.title("Alex, Berta, Chris und Doris 🐢")
wn.tracer(0)

d = 75
theta = 25
turtles = []

alex = t.Turtle()
alex.hideturtle()
alex.pencolor("#325069")
alex.pensize(2)
turtles.append(alex)

berta = t.Turtle()
berta.hideturtle()
berta.pencolor("#a0332e")
berta.pensize(2)
berta.left(-90)
turtles.append(berta)

chris = t.Turtle()
chris.hideturtle()
chris.pencolor("#8c5030")
chris.pensize(2)
chris.left(60)
chris.hideturtle()
turtles.append(chris)

doris = t.Turtle()
doris.hideturtle()
doris.pencolor("#d79e28")
doris.pensize(2)
doris.left(-60)
turtles.append(doris)

for i in range(180):
    for j in range(4):
        for turtle in turtles:
            turtle.left(90)
            turtle.forward(d)
    for turtle in turtles:
        turtle.left(theta)
    d *= 1.003
    wn.update()  # Den gesamten Bildschirm neuzeichnen
    
print("Die Schildkröten sagen: »We did it, Babe!« 🐢")

wn.mainloop()