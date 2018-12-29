import turtle as t

startpoints = [[-300, 250], [-150, 250],
                [-300, 110], [-80, 110],
                [-300, -150], [50, -150]]

wn = t.Screen()
wn.title("Fibonacci Tree 1")

fib = t.Turtle()

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

n = 0
for startpoint in startpoints:
    x, y = startpoint
    n += 1
    fib.penup()
    fib.setpos(x, y)
    fib.pendown()
    drawfib(n, 30)

wn.mainloop()