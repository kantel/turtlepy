import turtle as t
import os
import math

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

wn = t.Screen()
wn.setup(width = 800, height = 400)
wn.colormode(255)
wn.bgpic("images/bluemarble.png")
wn.setworldcoordinates(-180, -90, 180, 90)
wn.title("Blue Marble")

# Berlin
lat = 52.518611
lon = 13.408333

# Kopenhagen
# lat = 55.675706
# lon = 12.578745

# Reykjavik
# lat = 64.1354800
# lon = -21.8954100

# Kairo
# lat = 30.056111
# lon = 31.239444

# New York
# lat = 40.712778
# lon = -74.005833

# Mexico-Stadt
# lat = 19.4326077
# lon = -99.133208

# Sidney
# lat = -33.867487
# lon = 151.206990

# Tokyo
# lat = 35.6894875
# lon = 139.6917064

# ISS
# lat = 20.3404
# lon = -74.5908

lat1 = lat - math.cos(lat)

cap = t.Turtle()
cap.penup()
cap.goto(lon, lat)
cap.color("yellow")
cap.shape("circle")
cap.shapesize(0.2)
cap.stamp()
cap.color("red")
cap.goto(lon, lat1)
cap.stamp

wn.mainloop()
