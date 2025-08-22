import turtle as t

WIDTH, HEIGHT = 640, 400
BORDER = 20
BORDER2 = BORDER + 10

wn = t.Screen()
wn.setup(width=WIDTH, height=HEIGHT, startx=2000, starty=80)
wn.colormode(255)                                    # für Trinket auskommentieren
wn.title("Turtle Graphics Game Tutorial – Stage 1")  # für Trinket auskommentieren
wn.bgcolor("black")


class Sprite(t.Turtle):

    def __init__(self, tshape, tcolor):
        t.Turtle.__init__(self)
        self.penup()
        self.shape(tshape)
        self.color(tcolor)
        self.speed = 2
        self.max_speed = 10

    def move(self):
        self.forward(self.speed)

        # Ränder checken und ausweichen
        if self.xcor() >= WIDTH / 2 - BORDER2 or self.xcor() <= -WIDTH / 2 + BORDER2:
            self.forward(-self.speed)
            self.left(75)
        if self.ycor() >= HEIGHT / 2 - BORDER2 or self.ycor() <= -HEIGHT / 2 + BORDER2:
            self.forward(-self.speed)
            self.left(75)


class Actor(Sprite):

    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def move_faster(self):
        self.speed += 1
        # Geschwindigkeitsbegrenzug
        if abs(self.speed) > self.max_speed:
            self.speed = self.max_speed

    def move_slower(self):
        # Geschwindigkeitsbegrenzung
        self.speed -= 1
        if self.speed <= 0:
            self.speed = 0


class GameWorld(t.Turtle):

    def __init__(self):
        t.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(3)

    def draw_border(self):
        self.penup()
        self.goto(-WIDTH / 2 + BORDER, -HEIGHT / 2 + BORDER)
        self.pendown()
        self.goto(-WIDTH / 2 + BORDER, HEIGHT / 2 - BORDER)
        self.goto(WIDTH / 2 - BORDER, HEIGHT / 2 - BORDER)
        self.goto(WIDTH / 2 - BORDER, -HEIGHT / 2 + BORDER)
        self.goto(-WIDTH / 2 + BORDER, -HEIGHT / 2 + BORDER)


world = GameWorld()
world.draw_border()
player = Actor("classic", "red")


def exitGame():
    global keepGoing
    print("Bye, Bye, Baby!")
    keepGoing = False


# Auf Tastaturereignisse lauschen
wn.listen()
wn.onkey(player.turnleft, "Left")
wn.onkey(player.turnright, "Right")
wn.onkey(player.move_faster, "Up")
wn.onkey(player.move_slower, "Down")
wn.onkey(exitGame, "Escape")  # Escape beendet das Spiel

# Spiel-Schleife
keepGoing = True
while keepGoing:
    player.move()