import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.setup(width = 640, height = 400)
wn.title("Fibonacci Tree 2")

fib = t.Turtle()
fib.speed(0)
fib.pencolor(0, 255, 0)

def drawfib(n, len_ang):
    fib.forward(2*len_ang)
    if n == 0:
        pass
    elif n == 1:
        pass
    else:
        fib.left(len_ang)
        drawfib(n-1, len_ang)
        fib.right(2*len_ang)
        drawfib(n-2, len_ang)
        fib.left(len_ang)
    fib.backward(2*len_ang)

fib.penup()
fib.sety(-150)
fib.pensize(1)
fib.left(90)
fib.pendown()
drawfib(15, 10)

wn.mainloop()