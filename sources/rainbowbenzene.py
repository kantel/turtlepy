import turtle as t

wn = t.Screen()
wn.setup(width = 800, height = 800)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Regenbogen-Hexagon")

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

alex = t.Turtle()
alex.speed(0)
for i in range(360):
    alex.pencolor(colors[i%6])
    alex.width(i/100 + 1)
    alex.forward(i)
    alex.left(59)

print("I did it, Babe!")

wn.mainloop()