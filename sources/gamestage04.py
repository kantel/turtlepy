import turtle as t
import random as r
import math
import os

WIDTH = 600
HEIGHT = 600
NUMGOALS =  6  # Test: 4
NUMALIENS = 4  # Test: 2
NUMPARTICLES = 20

class Sprite(t.Turtle):
    
    def __init__(self, tshape, tcolor):
        t.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(tshape)
        self.color(tcolor)
        self.speed = 1
        self.max_speed = 15
    
    def move(self):
        self.forward(self.speed)

        # Ränder checken und ausweichen
        if self.xcor() >= WIDTH/2 - 50 or self.xcor() <= -WIDTH/2 + 50:
            self.forward(-self.speed)
            self.left(r.randint(95, 265))
        if self.ycor() >= HEIGHT/2 - 50 or self.ycor() <= -HEIGHT/2 + 50:
            self.forward(-self.speed)
            self.left(r.randint(95, 265))
    
    def collides(self, obj):
        a = self.xcor() - obj.xcor()
        b = self.ycor() - obj.ycor()
        distance =  math.sqrt((a**2) + (b**2))
        if distance < 20:
            return True
        else:
            return False
    
    def jump(self):
        self.goto(r.randint(-WIDTH/2 + 60, WIDTH/2 - 60),
                  r.randint(-HEIGHT/2 + 60, HEIGHT/2 - 60))
        self.setheading(r.randint(0, 360))
        self.speed = r.randint(2, 7)
 
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
        self.color = tcolor  # Wird im Programm überschrieben
        self.shapesize(stretch_wid = 0.6, stretch_len = 1.1, outline = None)
        self.speed = 5
    
    def turnleft(self):
        self.left(15)
    
    def turnright(self):
        self.right(15)
    
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

class Missile(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None)
        self.speed = 20   # So ein Geschoß sollte schon schnell sein :o)
        self.status = "ready"
        self.goto(-5000, -5000)
    
    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
        
    def move(self):
        if self.status == "ready":
            self.goto(-5000, -5000)
        if self.status == "firing":
            self.forward(self.speed)
            # Ränder checken und ausweichen
            if (self.xcor() >= WIDTH/2 - 50 or self.xcor() <= -WIDTH/2 + 50
            or self.ycor() >= HEIGHT/2 - 50 or self.ycor() <= -HEIGHT/2 + 50):
                self.goto(-5000, -5000)
                self.status = "ready"

class Pumpkin(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.speed = 3   # Default-Vorbelegung, wird bei der Initialisierung überschrieben
        self.goto(r.randint(-WIDTH/2 + 60, WIDTH/2 - 60),
                  r.randint(-HEIGHT/2 + 60, HEIGHT/2 - 60))
        self.setheading(r.randint(0, 360))

class Alien(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.speed = 3   # Default-Vorbelegung, wird bei der Initialisierung überschrieben
        self.goto(r.randint(-WIDTH/2 + 60, WIDTH/2 - 60),
                  r.randint(-HEIGHT/2 + 60, HEIGHT/2 - 60))
        self.setheading(r.randint(0, 360))

class Particle(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        stretch = r.uniform(0.1, 0.2)
        self.shapesize(stretch_wid = stretch, stretch_len = stretch, outline = None)
        self.goto(-5000, -5000)
        self.frame = 0
        self.speed = r.randint(10, 20)
    
    def explode(self, x, y):
        self.goto(x, y)
        self.setheading(r.randint(0, 360))
    
    def move(self):
        if self.frame < 20:
            self.forward(self.speed)
            # self.speed -= 1
            self.frame += 1
            # Ränder checken
            if (self.xcor() >= WIDTH/2 - 50 or self.xcor() <= -WIDTH/2 + 50 or
                self.ycor() >= HEIGHT/2 - 50 or self.ycor() <= -HEIGHT/2 + 50):
                self.frame = 0
                self.goto(-5000, -5000)
        else:
            self.frame = 0
            self.goto(-5000, -5000)
         
wn = t.Screen()
wn.bgcolor("#2b3e50")
path_to_bg = os.path.join(os.getcwd(), "sources/images/moon.gif")
wn.bgpic(path_to_bg)
pumpkin = os.path.join(os.getcwd(), "sources/images/pumpkin.gif")
alien = os.path.join(os.getcwd(), "sources/images/alien.gif")
wn.register_shape(pumpkin)
wn.register_shape(alien)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Space War – Halloween-Version")

# Bildschirm-Refresh ausschalten
wn.tracer(0)

player = Actor("triangle", "red")
missile = Missile("triangle", "yellow")
world = GameWorld()
hud = HeadUpDisplay()

# Die Grenzen des Spielfeldes zeichnen
world.draw_border()

# Die Zielobjekte erzeugen
pumpkins = []
for i in range(NUMGOALS):
    pumpkins.append(Pumpkin(pumpkin, "gold"))
    pumpkins[i].speed = r.randint(2, 7)

# Die Aliens erzeugen
aliens = []
for i in range(NUMALIENS):
    aliens.append(Alien(alien, "blue"))
    aliens[i].speed = r.randint(2, 7)
    
# Die Partikel erzeugen
particles = []
colors = ["red", "green", "violet", "blue", "yellow", "orange", "gold"]
for i in range(NUMPARTICLES):
    particles.append(Particle("circle", r.choice(colors)))

def exitGame():
    global keepGoing
    keepGoing = False

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(player.turnleft, "Left")
t.onkey(player.turnright, "Right")
t.onkey(player.move_faster, "Up")
t.onkey(player.move_slower, "Down")
t.onkey(missile.fire, "space")
t.onkey(exitGame, "Escape") # Escape beendet das Spiel

# Spiel-Schleife
keepGoing = True
while keepGoing:
    wn.update()  # Den gesamten Bildschirm neuzeichnen
    player.move()
    missile.move()
    hud.change_score(0)
    
    for pumpkin in pumpkins:
        pumpkin.move()
        if missile.collides(pumpkin):
            pumpkin.jump()
            missile.status = "ready"
            hud.change_score(-10)
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
        if player.collides(pumpkin):
            pumpkin.jump()
            hud.change_score(10)
            for particle in particles:
                particle.explode(player.xcor(), player.ycor())
    
    for alien in aliens:
        alien.move()
        if missile.collides(alien):
            alien.jump()
            missile.status = "ready"
            hud.change_score(20)
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
        if player.collides(alien):
            alien.jump()
            hud.change_score(-20)
            for particle in particles:
                particle.explode(player.xcor(), player.ycor())
            
    for particle in particles:
        particle.move()
            
    if hud.score < 0:
        print("You lost the game!")
        # keepGoing = False
