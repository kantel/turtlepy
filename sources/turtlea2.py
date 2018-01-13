import turtle

wn = turtle.Screen()
colors = ["orange", "forest green", "deep sky blue", "gold", "red", "sienna"]
t = turtle.Turtle()
t.color("red")
i = 0
t.speed(0)    # 3 ist die Default-Geschwindigkeit der Turtle, 0 ist die schnellste
for angle in range(0, 360, 5):
    t. color(colors[i % 6])
    t.seth(angle)
    t.circle(100)
    i += 1

wn.mainloop()