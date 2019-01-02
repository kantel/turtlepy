import turtle as t

WIDTH = 500
HEIGHT = 500

# Initialisierung
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(235, 215, 182)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Beautiful Flower")

flower = t.Turtle()
flower.speed(0)
flower.pencolor(0, 200, 0)
flower.pensize(2)

def draw_figure(size, angle, turn):
    if size < 10:
        return
    while True:
        draw_flower(size, angle)
        turn += angle
        if turn % 360 == 0:
            break

def draw_flower(size, angle):
    flower.forward(size)
    flower.pencolor(200, 0, 0)
    flower.dot(15)
    flower.pencolor(0, 200, 0)
    draw_figure(size/2, -angle, 0)
    flower.right(angle)

flower.penup()
flower.setpos(-40, 64)
flower.pendown()
draw_figure(64, 60, 0)
flower.hideturtle()

print("I did it, Babe!")        

wn.mainloop()