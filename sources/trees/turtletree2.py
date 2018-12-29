import turtle as t

WIDTH = 600
HEIGHT = 420

# Initialisierung
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(235, 215, 182)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Fractal Tree 2")

ftree = t.Turtle()
ftree.speed(0)
ftree.pencolor(0, 100, 0)
ftree.setheading(90)

def draw_tree(n):
    if (n < 3):
        return
    else:
        ftree.pensize(n/10 + 1)
        ftree.forward(n)
        ftree.left(30)
        draw_tree(3*n/4)
        ftree.right(60)
        draw_tree(3*n/4)
        ftree.left(30)
        ftree.backward(n)

ftree.penup()
ftree.setpos(0, -180)
ftree.pendown()

# Bildschirm-Refresh ausschalten
wn.tracer(0)
draw_tree(100)
ftree.hideturtle()
# Bildschirm-Refresh wieder einschalten
wn.update()

wn.mainloop()