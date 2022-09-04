import turtle as t

WIDTH = 400
HEIGHT = 420

# Initialisierung
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(235, 215, 182)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Fractal Tree")

ftree = t.Turtle()
ftree.speed(0)
ftree.pencolor(0, 100, 0)
ftree.pensize(1)
ftree.setheading(90)

def draw_tree(n):
    if (n < 5):
        ftree.forward(n)
        ftree.backward(n)
        return
        
    ftree.forward(n/3)
    ftree.left(30)
    draw_tree(n*2/3)
    ftree.right(30)
    ftree.forward(n/6)
    ftree.right(25)
    draw_tree(n/2)
    ftree.left(25)
    ftree.forward(n/3)
    ftree.right(25)
    draw_tree(n/2)
    ftree.left(25)
    ftree.forward(n/6)
    ftree.backward(n)


# Bildschirm-Refresh ausschalten
wn.tracer(0)
ftree.penup()
ftree.setpos(20, -175)
ftree.pendown()
draw_tree(250)
ftree.hideturtle()
# Bildschirm-Refresh wieder einschalten
wn.update()

wn.mainloop()