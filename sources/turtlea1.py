import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.color("red")
t.speed(0)    # 3 ist die Default-Geschwindigkeit der Turtle, 0 ist die schnellste
for angle in range(0, 360, 5):
    t.seth(angle)
    t.circle(100)

wn.mainloop()