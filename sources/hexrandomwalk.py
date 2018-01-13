import turtle as t
import random as r

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Hexagonaler Random Walk")

hexi = t.Turtle()
hexi.speed(0)
hexi.pensize(2)


for step in range(1000):
    if step < 200:
        hexi.pencolor(255, 255, 178)
    elif step < 400:
        hexi.pencolor(254, 204, 92)
    elif step < 600:
        hexi.pencolor(253, 141, 60)
    elif step < 800:
        hexi.pencolor(240, 59, 32)
    else:
        hexi.pencolor(189, 0, 38)
    roll = r.randint(1, 6)
    if roll == 1:
        hexi.seth(0)
    elif roll == 2:
        hexi.seth(60)
    elif roll == 3:
        hexi.seth(120)
    elif roll == 4:
        hexi.seth(180)
    elif roll == 5:
        hexi.seth(240)
    elif roll == 6:
        hexi.seth(300)
    else:
        print("Es ist etwas faul im Staate Dänemark!")
    hexi.fd(10)

print("I did it, Babe!")

wn.mainloop()