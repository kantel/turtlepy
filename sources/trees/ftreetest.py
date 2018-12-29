import turtle as t

WIDTH = 600
HEIGHT = 600

# Initialisierung
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(255, 255, 255)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Fractal Tree")

ftree = t.Turtle()
# ftree.speed(0)
ftree.pencolor(0, 255, 0)
ftree.pensize(1)


ftree.penup()
ftree.sety(-280)
ftree.pendown()
ftree.forward(100)
print(ftree.position())


wn.mainloop()