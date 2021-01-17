import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Ein Hexagon mit der Schildkröte")

hexi = t.Turtle()
hexi.pensize(2)
hexi.pencolor(253, 141, 60)

hexi.penup()
hexi.goto(-62, -87)  # Hexagon im Fenster »einmitten«
hexi.pendown()

hexi.forward(100)
hexi.left(60)
hexi.forward(100)
hexi.left(60)
hexi.forward(100)
hexi.left(60)
hexi.forward(100)
hexi.left(60)
hexi.forward(100)
hexi.left(60)
hexi.fd(100)
hexi.left(60)

print("I did it, Babe!")

wn.mainloop()