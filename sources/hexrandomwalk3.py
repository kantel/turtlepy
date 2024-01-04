import turtle as t
import random as r

WIDTH = 540
HEIGHT = 640
MIN_X = -WIDTH//2 + 10
MAX_X = WIDTH//2 - 20
MIN_Y = HEIGHT//2 - 10
MAX_Y = -HEIGHT//2 + 20 
STEPSIZE = 20
BORDERSIZE = 1

codingtrain = ["#f05025", "#f89e50", "#f8ef22", "#f063a4",
               "#9252a1", "#817ac6", "#62c777", "#31c5f4"]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor("#2a282d")
wn.setup(width = WIDTH, height = HEIGHT, startx = 1300, starty = 30)
wn.title("🐢 Hexagonaler Random Walk 🐢")

# Draw Border
border = t.Turtle()
border.speed(0)
border.pensize(BORDERSIZE)
border.pencolor("#e6e2cc")
border.penup()
border.hideturtle()
border.goto(MIN_X, MIN_Y)
border.pendown()
border.goto(MAX_X, MIN_Y)
border.goto(MAX_X, MAX_Y)
border.goto(MIN_X, MAX_Y)
border.goto(MIN_X, MIN_Y)

# Start Random Walk
hexi = t.Turtle()
hexi.speed(0)
hexi.pensize(2)

for step in range(5000):

    # Set Poncolor
    if step%20 == 0:
        hexi.pencolor(codingtrain[r.randint(0, len(codingtrain) - 1)])

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
    if hexi.xcor() >= MAX_X - STEPSIZE:
        # hexi.penup()
        # hexi.setx(MIN_X + STEPSIZE)
        # hexi.pendown()
        STEPSIZE *= -1
        hexi.fd(STEPSIZE)
    elif hexi.xcor() <= MIN_X + STEPSIZE: 
        # hexi.penup()
        # hexi.setx(MAX_X - STEPSIZE)
        # hexi.pendown()
        STEPSIZE *= -1
        hexi.fd(STEPSIZE)
    elif hexi.ycor() <= MAX_Y + STEPSIZE:
        # hexi.penup()
        # hexi.sety(MIN_Y - STEPSIZE)
        # hexi.pendown()
        STEPSIZE *= -1
        hexi.fd(STEPSIZE)
    elif hexi.ycor() >= MIN_Y - STEPSIZE:
        # hexi.penup()
        # hexi.sety(MAX_Y + STEPSIZE)
        # hexi.pendown()
        STEPSIZE *= -1
        hexi.fd(STEPSIZE)
    else:
        hexi.fd(STEPSIZE)

print("I did it, Babe!")
wn.exitonclick()

wn.mainloop()