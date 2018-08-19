# Space Invaders Stage 2: Die Spielewelt zeichnen

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


# Initialisierung

wn = t.Screen()
wn.bgcolor("#000000")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Space Invaders – Stage 2")

# Bildschirm-Refresh ausschalten
wn.tracer(0)


# Objekte initialisieren
world = GameWorld()
world.draw_border()

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(world.exit_game, "Escape") # Escape beendet das Spiel


while world.keepGoing:
    wn.update()  # Bildschirm-Refresh einschalten und den gesamten Bildschirm neuzeichnen
