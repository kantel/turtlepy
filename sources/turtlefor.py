import turtle as t

wn = t.Screen()
wn.bgcolor("green")
wn.setup(width = 640, height = 400)
wn.title("Atari!")
alex = t.Turtle()
alex.pencolor("black")
alex.pensize(2)

for i in range(4):
    alex.left(90)
    alex.forward(100)

print("Schildkröte Alex sagt: »I did it, Babe!« 🐢")

wn.mainloop()