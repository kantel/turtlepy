import turtle as t
import os
import os.path

WIDTH = 600
HEIGHT = 600

wn = t.Screen()
wn.bgcolor("#2b3e50")
path_to_bg1 = os.path.join(os.getcwd(), "sources/turtle/images/space.gif")
path_to_bg2 = os.path.join(os.path.abspath(os.curdir), "images/space.gif")
print(path_to_bg1)
print(path_to_bg2)
wn.bgpic(path_to_bg1)
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Pfade finden")

wn.mainloop()