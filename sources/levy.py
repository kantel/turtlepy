import turtle as t

wn = t.Screen()
wn.setup(width = 640, height = 480)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Lévy-Kurve")

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

paul.goto(125, 80)
# wn.tracer(0)
paul.pendown()
levy(12, 4)
# wn.update()

print("I did it, Babe!")

wn.mainloop()
