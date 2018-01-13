import turtle as t
import random as r
import os
import math

wn = t.Screen()
wn.bgcolor("black")
wn.title("In den Labyrinthen von Buchhaim – Stage 2")
wn.setup(640, 480)

wall_shape = os.path.join(os.getcwd(), "sources/roguelike/images/wall.gif")
player_shape = os.path.join(os.getcwd(), "sources/roguelike/images/player.gif")
gold1_shape = os.path.join(os.getcwd(), "sources/roguelike/images/gold1.gif")
gold2_shape = os.path.join(os.getcwd(), "sources/roguelike/images/gold2.gif")
gold3_shape = os.path.join(os.getcwd(), "sources/roguelike/images/gold3.gif")
gold4_shape = os.path.join(os.getcwd(), "sources/roguelike/images/gold4.gif")
gold5_shape = os.path.join(os.getcwd(), "sources/roguelike/images/gold5.gif")
gold6_shape = os.path.join(os.getcwd(), "sources/roguelike/images/gold6.gif")
wn.register_shape(wall_shape)
wn.register_shape(player_shape)
wn.register_shape(gold1_shape)
wn.register_shape(gold2_shape)
wn.register_shape(gold3_shape)
wn.register_shape(gold4_shape)
wn.register_shape(gold5_shape)
wn.register_shape(gold6_shape)

# Die Oberklasse Sprite, zugleich die Klasse für die Mauern des Labyrinths
class Sprite(t.Turtle):
    
    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)
    
    def collides_with(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt(a**2 + b**2)
        if distance < 5:
            return True
        else:
            return False
    
    def destroy(self):
        self.goto(5000, 5000)
        self.hideturtle()

# Der Spieler
class Player(Sprite):
    
    def __init__(self, shape):
        Sprite.__init__(self, shape)
        self.gold = 0
    
    def go_left(self):
        go_to_x = self.xcor() - 32
        go_to_y = self.ycor()
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)
        
    def go_right(self):
        go_to_x = self.xcor() + 32
        go_to_y = self.ycor()
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

    def go_up(self):
        go_to_x = self.xcor()
        go_to_y = self.ycor() + 32
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)
        
    def go_down(self):
        go_to_x = self.xcor()
        go_to_y = self.ycor() - 32
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

# Die Schätze
class Treasure(Sprite):
    
    def __init__(self, shape, x, y, amount):
        Sprite.__init__(self, shape)
        self.x = x
        self.y = y
        self.gold = amount
        self.goto(self.x, self.y)

# Listen der Labyrinthe, der Mauern und der Schätze
levels = []
walls = []
treasures = []
treasure_shapes = [gold1_shape, gold2_shape, gold3_shape,
                   gold4_shape, gold5_shape, gold6_shape]

level_1 = [
    "####################",
    "# @#               #",
    "#  #######  #####  #",
    "#        #  #g     #",
    "#        #  #####  #",
    "#######  #  #      #",
    "#        #  #####  #",
    "#  #######    #    #",
    "#             #   g#",
    "#  #################",
    "#                  #",
    "####  ###########  #",
    "#           g#     #",
    "#            #g    #",
    "####################"
]

levels.append(level_1)

# Level Setup
def setup_maze(level):
    global num_treasures
    for y in range(len(level)):
        for x in range(len(level[y])):
            sprite= level[y][x]
            screen_x = -308 + (x*32)
            screen_y =  224 - (y*32)
            
            if sprite == "#":
                wall.goto(screen_x, screen_y)
                walls.append((screen_x, screen_y))
                wall.stamp()
            elif sprite == "@":
                rogue.goto(screen_x, screen_y)
                rogue.stamp
            elif sprite == "g":
                treasures.append(Treasure(r.choice(treasure_shapes), screen_x, screen_y, r.randint(25, 250)))
                num_treasures += 1

def exitGame():
    global keepGoing
    keepGoing = False

wall = Sprite(wall_shape)
rogue = Player(player_shape)

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(rogue.go_left, "Left")
t.onkey(rogue.go_right, "Right")
t.onkey(rogue.go_up, "Up")
t.onkey(rogue.go_down, "Down")
t.onkey(exitGame, "Escape") # Escape beendet das Spiel

wn.tracer(0)
num_treasures = 0
setup_maze(levels[0])
# print(walls)

keepGoing = True
while keepGoing:
    for treasure in treasures:
        if rogue.collides_with(treasure):
            rogue.gold += treasure.gold
            print("Goldschatz des Spielers: {} Goldstücke".format(rogue.gold))
            treasure.destroy()
            num_treasures -= 1
            if num_treasures == 0:
                print("Glückwunsch, Du hast diesen Level überlebt!")
    wn.update()
