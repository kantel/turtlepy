import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("red")

tess.penup()
size = 10
for i in range(120):
   tess.stamp()
   size += 1
   tess.forward(size)
   tess.right(24)

wn.mainloop()