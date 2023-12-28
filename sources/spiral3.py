import turtle as t

WIDTH = 600
HEIGHT = 600

pal = [(173, 154, 133), (185, 217, 225), (229, 171, 115), (227, 214, 173),
       (68, 140, 140), (223, 216, 196)]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(41, 37, 33)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Sechseck-Spirale")

p = t.Turtle()
p.width(2)
p.speed(0)
p.hideturtle()

# Sechseck
for i in range(300):
    p.color(pal[i%6])
    p.forward(i*0.9)
    p.right(61)

print("I did it, Babe!")

wn.mainloop()