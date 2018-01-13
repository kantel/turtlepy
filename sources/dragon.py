import turtle as t
import math

numgen = 12

wn = t.Screen()
wn.setup(width = 640, height = 400)
wn.colormode(255)
wn.bgcolor(50, 50, 50)
wn.title("Drachenkurve")

puff = t.Turtle()
puff.speed(0)
puff.pencolor(150, 255, 100)
# puff.shape("turtle")

def dragon(drag, s, n, flag):
    if n == 0:
        drag.forward(s)
    else:
        alpha = 45
        if flag == 1:
            alpha = -alpha
            flag = -flag
        drag.left(alpha)
        dragon(drag, s/math.sqrt(2), n-1, -flag)
        drag.right(2*alpha)
        dragon(drag, s/math.sqrt(2), n-1, flag)
        drag.left(alpha)

puff.penup()
puff.setpos(-125, 50)
puff.pendown()
dragon(puff, 300, numgen, 1)
print("I did it, Babe!")

wn.mainloop()