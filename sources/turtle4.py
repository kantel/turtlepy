import turtle as t

wn = t.Screen()
wn.bgcolor("green")
wn.setup(width = 640, height = 400)
wn.title("Alex, Berta, Chris und Doris")

alex = t.Turtle()
alex.pencolor("black")
alex.pensize(2)

berta = t.Turtle()
berta.pencolor("red")
berta.pensize(2)
berta.left(-90)

chris = t.Turtle()
chris.pencolor("blue")
chris.pensize(2)
chris.left(60)

doris = t.Turtle()
doris.pencolor("brown")
doris.pensize(2)
doris.left(-60)

# i = 0
for i in range(4):
    alex.left(90)
    alex.forward(100)
    berta.left(90)
    berta.forward(100)
    chris.left(90)
    chris.forward(100)
    doris.left(90)
    doris.forward(100)

print("Die Schildkröten sagen: »We did it, Babe!« 🐢")

wn.mainloop()