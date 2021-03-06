import turtle as t
import random as r
import math

WIDTH = 640
HEIGHT = 480
NUMGOALS = 6

class Sprite(t.Turtle):
    
    def __init__(self, tshape, tcolor):
        t.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(tshape)
        self.color(tcolor)
        self.speed = 1
        self.max_speed = 10
    
    def move(self):
        self.forward(self.speed)

        # Ränder checken und ausweichen
        if self.xcor() >= WIDTH/2 - 50 or self.xcor() <= -WIDTH/2 + 50:
            self.forward(-self.speed)
            self.left(75)
        if self.ycor() >= HEIGHT/2 - 50 or self.ycor() <= -HEIGHT/2 + 50:
            self.forward(-self.speed)
            self.left(75)
    

class GameWorld(t.Turtle):
    
    def __init__(self):
        t.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(2)
    
    def draw_border(self):
        self.penup()
        self.goto(-WIDTH/2 + 40, -HEIGHT/2 + 40)
        self.pendown()
        self.goto(-WIDTH/2 + 40, HEIGHT/2 - 40)
        self.goto(WIDTH/2 - 40, HEIGHT/2 - 40)
        self.goto(WIDTH/2 - 40, -HEIGHT/2 + 40)
        self.goto(-WIDTH/2 + 40, -HEIGHT/2 + 40)

class HeadUpDisplay(t.Turtle):
    
    def __init__(self):
        t.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-WIDTH/2 + 40, HEIGHT/2 - 30)
        self.score = 0
    
    def update_score(self):
        self.clear()
        self.write("Punkte: {}".format(self.score), False, align = "left",
                    font = ("Arial", 14, "normal"))
    
    def change_score(self, points):
        self.score += points
        self.update_score()


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
        if abs(self.speed) > self.max_speed:
            self.speed = - self.max_speed
            
    def collides(self, obj):
        a = self.xcor() - obj.xcor()
        b = self.ycor() - obj.ycor()
        distance =  math.sqrt((a**2) + (b**2))
        if distance < 20:
            return True
        else:
            return False

class Goal(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.speed = 3   # Default-Vorbelegung, wird bei der Initialisierung überschrieben
        self.goto(r.randint(-WIDTH/2 + 60, WIDTH/2 - 60),
                  r.randint(-HEIGHT/2 + 60, HEIGHT/2 - 60))
        self.setheading(r.randint(0, 360))
    
    def jump(self):
        self.goto(r.randint(-WIDTH/2 + 60, WIDTH/2 - 60),
                  r.randint(-HEIGHT/2 + 60, HEIGHT/2 - 60))
        self.setheading(r.randint(0, 360))
        


wn = t.Screen()
wn.bgcolor("black")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Turtle Graphics Game Tutorial – Stage 2")

player = Actor("triangle", "red")
world = GameWorld()
hud = HeadUpDisplay()

# Die Grenzen des Spielfeldes zeichnen
world.draw_border()

# Die Zielobjekte erzeugen
goals = []
for i in range(NUMGOALS):
    goals.append(Goal("circle", "gold"))
    goals[i].speed = r.randint(2, 7)

def exitGame():
    global keepGoing
    keepGoing = False

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(player.turnleft, "Left")
t.onkey(player.turnright, "Right")
t.onkey(player.move_faster, "Up")
t.onkey(player.move_slower, "Down")
t.onkey(exitGame, "Escape") # Escape beendet das Spiel

# Bildschirm-Refresh ausschalten
wn.tracer(0)

# Spiel-Schleife
keepGoing = True
while keepGoing:
    wn.update()  # Den gesamten Bildschirm neuzeichnen
    player.move()
    hud.change_score(0)
    
    for goal in goals:
        goal.move()
        if player.collides(goal):
            goal.jump()
            hud.change_score(10)
