import turtle

WIDTH, HEIGHT = 640, 400
factor = 0.6

wn = turtle.Screen()
wn.setup(width = WIDTH, height = HEIGHT, startx = 2000, starty = 80)
wn.title("Fractal Tree")   # Für Trinket auskommentieren
wn.colormode(255)          # Für Trinket auskommentieren
wn.bgcolor(222, 217, 177)
wn.tracer(0)

alice = turtle.Turtle()
alice.speed(0) # Schnelle Geschwindigkeit
alice.hideturtle()
alice.penup()
alice.goto(0, -160)
alice.left(90) # Nach oben ausrichten
alice.pendown()

def fractal_tree(laenge, tiefe):
    if tiefe == 0 or laenge < 1: # Basis der Rekursion
        return
    alice.pensize(max(laenge/42.0, 1))
    # Farben in Abängigkeit von der Dicke des Stammes
    if laenge >= 70:
        alice.pencolor(139, 69, 19)
    elif laenge >= 2:
        alice.pencolor(85, 107, 47)
    else:
        alice.pencolor(139, 69, 19)

    alice.forward(laenge * factor // 3)
    alice.left(45) # Nach links drehen
    fractal_tree(laenge * factor, tiefe - 1) # Rekursiver Aufruf
    alice.right(90) # Nach rechts drehen
    fractal_tree(laenge * factor, tiefe - 1) # Rekursiver Aufruf
    alice.left(45) # Zurück zur Ausrichtung des Elternastes
    # Auf dem Rückweg durch die Rekursion
    alice.backward(laenge * factor // 3)

fractal_tree(650, 12)
wn.update()

print("I did it, Babe!")
wn.mainloop()