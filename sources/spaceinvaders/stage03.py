# Space Invaders Stage 3: Die Klasse Sprite und den Spieler hinzufügen

import turtle as t

# Fenstergröße
WIDTH = 700
HEIGHT = 700
# Weltgröße
WW = 600
WH = 600

# Hier kommen die Klassendefinitionen hin

class GameWorld(t.Turtle):
    
    def __init__(self):
        t.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(3)
        self.keepGoing = True
    
    def draw_border(self):
        self.penup()
        self.goto(-WW/2, -WH/2)
        self.pendown()
        for i in range(4):
            self.forward(WW)
            self.left(90)

    def exit_game(self):
        self.keepGoing = False


class Sprite(t.Turtle):
    
    def __init__(self, tshape, tcolor):
        t.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(tshape)
        self.color(tcolor)
        self.speed = 1

class Actor(Sprite):
    
    def __init__(self, tshape, tcolor):
        Sprite.__init__(self, tshape, tcolor)
        self.speed = 10
        self.x = 0
        self.y = -280
        self.setheading(90)
        self.goto(self.x, self.y)
        
    def go_left(self):
        self.x -= self.speed
        if self.x <= -WW/2 + 20:
            self.x = -WW/2 + 20
        self.setx(self.x)

    def go_right(self):
        self.x += self.speed
        if self.x >= WW/2 - 20:
            self.x = WW/2 - 20
        self.setx(self.x)

# Initialisierung

wn = t.Screen()
wn.bgcolor("#000000")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Space Invaders – Stage 3")

# Bildschirm-Refresh ausschalten
wn.tracer(0)


# Objekte initialisieren
world = GameWorld()
world.draw_border()
player = Actor("triangle", "purple")

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(player.go_left, "Left")
t.onkey(player.go_right, "Right")
t.onkey(world.exit_game, "Escape") # Escape beendet das Spiel

while world.keepGoing:
    wn.update()  # Bildschirm-Refresh einschalten und den gesamten Bildschirm neuzeichnen
