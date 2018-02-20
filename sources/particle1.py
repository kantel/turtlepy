import turtle as t
from particle import Particle

wn = t.Screen()
wn.setup(width = 500, height = 400)
wn.colormode(255)
wn.bgcolor(0, 0, 0)
wn.title("Particle-System")

# Bildschirm-Refresh ausschalten
wn.tracer(0)

def exit_sim():
    global keepGoing
    keepGoing = False


t.listen()
t.onkey(exit_sim, "Escape") # Escape beendet die Simulation

particles = []
keepGoing = True
while keepGoing:
    wn.update()  # Den gesamten Bildschirm neuzeichnen
    p = Particle("circle", (255, 0, 0), 0, -120)
    particles.append(p)
    for i in range(len(particles)-1, 0, -1):
        particles[i].update()
        if particles[i].isDead():
            particles.pop(i)
            # print(len(particles))
