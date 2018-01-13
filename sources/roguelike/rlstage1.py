import turtle as t
import os


wn = t.Screen()
wn.bgcolor("black")
wn.title("In den Labyrinthen von Buchhaim – Stage 1")
wn.setup(640, 480)

wall_shape = os.path.join(os.getcwd(), "sources/roguelike/images/wall.gif")
player_shape = os.path.join(os.getcwd(), "sources/roguelike/images/player.gif")
wn.register_shape(wall_shape)
wn.register_shape(player_shape)


# Die Mauern des Labyrinths
class Sprite(t.Turtle):
    
    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)
    

class Player(Sprite):
    
    def __init__(self, shape):
        Sprite.__init__(self, shape)

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




# Liste der Labyrinthe
levels = []

level_1 = [
    "####################",
    "# @#               #",
    "#  #######  #####  #",
    "#        #  #      #",
    "#        #  #####  #",
    "#######  #  #      #",
    "#        #  #####  #",
    "#  #######    #    #",
    "#             #    #",
    "#  #################",
    "#                  #",
    "####  ###########  #",
    "#            #     #",
    "#            #     #",
    "####################"
]

levels.append(level_1)

# Level Setup
def setup_maze(level):
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

def exitGame():
    global keepGoing
    keepGoing = False

walls = []
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
setup_maze(levels[0])
# print(walls)

keepGoing = True
while keepGoing:
    wn.update()
