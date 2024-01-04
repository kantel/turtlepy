import turtle as t
import random as r

WIDTH = 600
HEIGHT = 600
STEPSIZE = 10

codingtrain = ["#f05025", "#f89e50", "#f8ef22", "#f063a4",
               "#9252a1", "#817ac6", "#62c777", "#31c5f4"]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor("#2a282d")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Hexagonaler Random Walk")

hexi = t.Turtle()
hexi.speed(0)
hexi.pensize(2)

for step in range(1600):

    # Set Poncolor
    if step < 200:
        hexi.pencolor(codingtrain[0])
    elif step < 400:
        hexi.pencolor(codingtrain[1])
    elif step < 600:
        hexi.pencolor(codingtrain[2])
    elif step < 800:
        hexi.pencolor(codingtrain[3])
    elif step < 1000:
        hexi.pencolor(codingtrain[4])
    elif step < 1200:
        hexi.pencolor(codingtrain[5])
    elif step < 1400:
        hexi.pencolor(codingtrain[6])
    else:
        hexi.pencolor(codingtrain[7])

    # Roll Dice and set Angle
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
    
    # Check Border
    if hexi.xcor() > WIDTH/2:
        hexi.penup()
        hexi.setx(-WIDTH/2)
        hexi.pendown()
    if hexi.xcor() < -WIDTH/2:
        hexi.penup()
        hexi.setx(WIDTH/2)
        hexi.pendown()
    if hexi.ycor() > HEIGHT/2:
        hexi.penup()
        hexi.sety(-HEIGHT/2)
        hexi.pendown()
    if hexi.ycor() < -HEIGHT/2:
        hexi.penup()
        hexi.sety(HEIGHT/2)
        hexi.pendown()

    hexi.fd(STEPSIZE)

print("I did it, Babe!")
wn.exitonclick()

wn.mainloop()