import turtle as t

WIDTH = 600
HEIGHT = 600

wn = t.Screen()
wn.bgcolor("white")  # alternativ: #2b3e50
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Turtle (Game) Template")

# Bildschirm Refresh ausschalten
wn.tracer(0)

# Das Programm beenden
def exit_prog():
    global keep_going
    keep_going = False

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(exit_prog, "Escape")  # Escape beendet das Programm

# Game Loop
keep_going = True
while keep_going:
    wn.update()  # Den gesamten Bildschirm neuzeichnen
