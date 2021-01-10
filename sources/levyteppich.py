import turtle as t

wn = t.Screen()
wn.setup(width = 640, height = 640)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Lévy-Teppich")

paul = t.Turtle()
paul.speed(0)
paul.pencolor(150, 255, 100)
paul.penup()
paul.hideturtle()

def levy(deg, len):
    if deg == 0:
        paul.forward(len)
    else:
        levy(deg-1, len)
        paul.right(90)
        levy(deg-1, len)
        paul.left(90)

paul.goto(125, 125)
wn.tracer(0)
paul.pendown()
levy(12, 4)

paul.pencolor(255, 100, 150)
paul.left(90)
levy(12, 4)

paul.pencolor(100, 150, 255)
paul.left(90)
levy(12, 4)

paul.pencolor(255, 150, 100)
paul.left(90)
levy(12, 4)
wn.update()

print("I did it, Babe!")

wn.mainloop()