import turtle as t

WIDTH = 600
HEIGHT = 600

pal = [(173, 154, 133), (185, 217, 225), (229, 171, 115), (227, 214, 173),
       (68, 140, 140), (223, 216, 196)]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(41, 37, 33)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Fünfeck-Spirale")

p = t.Turtle()
p.width(2)
p.speed(0)
p.hideturtle()

# Fünfeck
for i in range(300):
    p.color(pal[i%5])
    p.forward(i*1.1)
    p.right(73)

print("I did it, Babe!")

wn.mainloop()