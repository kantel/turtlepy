import turtle as t
import math
import os
import csv

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

wn = t.Screen()
wn.setup(width = 1000, height = 500)
wn.colormode(255)
wn.bgpic("images/earthmap.png")
wn.setworldcoordinates(-180, -90, 180, 90)
wn.title("Blue Marble")

city = t.Turtle()
city.penup()
city.color("red")
city.shape("circle")
city.shapesize(0.4)
wn.tracer(0)

file = open("cities.csv", "r")
cities = csv.reader(file, delimiter = ",")
for c in cities:
    # print(c[1], c[2])
    lat = float(c[1])
    # lat = lat - math.cos(lat)
    lon = float(c[2])
    city.goto(lon, lat)
    city.stamp()
    
file.close()
wn.update()

wn.mainloop()
