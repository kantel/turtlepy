import turtle as t
import random as r

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.setup(width = 640, height = 400)
wn.title("Fibonacci Tree 3")

fib = t.Turtle()
fib.speed(0)
fib.pencolor(0, 255, 0)

def drawfib(n, len_ang):
    ang = r.uniform(len_ang - 0.9, len_ang + 1.7)
    fib.forward(2*ang)
    if n == 0:
        pass
    elif n == 1:
        pass
    else:
        fib.left(ang)
        drawfib(n-1, ang)
        fib.right(2*ang)
        drawfib(n-2, ang)
        fib.left(ang)
    fib.backward(2*ang)

fib.penup()
fib.sety(-150)
fib.pensize(1)
fib.left(90)
fib.pendown()
drawfib(15, 10)

wn.mainloop()