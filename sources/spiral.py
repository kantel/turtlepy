import turtle as t

WIDTH = 600
HEIGHT = 600

pal = [(1, 155, 183), (226, 107, 67), (240, 192, 68), (144, 166, 215)]

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(4, 21, 31)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Bridget Riley Spirale")

p = t.Turtle()
p.width(2)
p.speed(0)
p.hideturtle()

# Dreieck
# for i in range(300):
#     p.color(pal[i%3])
#     p.forward(i*1.5)
#     p.right(121)

# Quadrat
for i in range(300):
    p.color(pal[i%4])
    p.forward(i*1.2)
    p.right(91)

print("I did it, Babe!")

wn.mainloop()