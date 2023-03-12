import turtle, math
import random
import os

WIDTH, HEIGHT = 440, 440
WALL   = 63
DOOR   = 62
CHEST  = 22
KEY    = 23
PLAYER = 10
ENEMY  = 12
TILESIZE = 16

maze_map_0 = [[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,10,-1,63,22,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,-1,-1,63],
            [63,-1,-1,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,63,63,-1,-1,63,22,63,63,63,63,-1,-1,63,63,63,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,63,63,-1,-1,63,-1,63,-1,-1,-1,-1,12,-1,-1,-1,-1,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63],
            [63,-1,-1,-1,-1,63,-1,-1,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,-1,63,63],
            [63,63,63,63,-1,63,-1,-1,63,63,-1,-1,-1,-1,63,-1,22,63,-1,-1,63,-1,-1,63,63],
            [63,23,-1,63,-1,63,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,-1,63,22,-1,63,-1,-1,63,63],
            [63,-1,-1,63,-1,63,-1,-1,63,63,63,63,63,63,63,-1,-1,63,63,63,63,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,-1,63,63,-1,-1,-1,-1,-1,-1,63],
            [63,12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,-1,12,-1,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,63,-1,-1,-1,63,-1,22,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,22,63,63,63,63,-1,-1,63,-1,63,63,63,-1,-1,63],
            [63,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,-1,63,63,63,63,-1,-1,63,63,63,63,63,63,63,63,63,63,-1,22,63],
            [63,63,63,63,63,-1,-1,-1,-1,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12,-1,63],
            [63,22,-1,-1,63,-1,-1,-1,-1,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,63,63,63,-1,22,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,12,-1,-1,-1,63,63,63,63,63,63,63,22,-1,-1,-1,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,-1,63,-1,-1,-1,-1,-1,-1,63],
            [63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62],
            [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63]]

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("🧙 Simple Maze Game Stage 3 🧙")
screen.bgcolor("#2b3e50")

# Bildschirm-Refresh ausschalten
screen.tracer(0)

DATAPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "data")

wall = os.path.join(DATAPATH, "wall1.gif")
wizard = os.path.join(DATAPATH, "wizard.gif")
enemy = os.path.join(DATAPATH, "enemy.gif")
chest = os.path.join(DATAPATH, "chest.gif")
key = os.path.join(DATAPATH, "key.gif")
door_open = os.path.join(DATAPATH, "door_open.gif")
door_closed = os.path.join(DATAPATH, "door_closed.gif")

# Die Turtle-Bilder registrieren
images = [wall, wizard, enemy, chest, key, door_open, door_closed]
for img in images:
    screen.register_shape(img)

class Sprite(turtle.Turtle):
  
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.right(270)
        self.speed(0)

  # Kollisionserkennung (Pythagoras)
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Player(Sprite):
  
    def __init__(self):
        Sprite.__init__(self)
        # self.start_x, self.start_y = 0, 0
        self.shape(wizard)
        self.gold = 0
        self.has_key = False
    
    # Player Movement
    def go_up(self):
        next_x, next_y = self.xcor(), self.ycor() + TILESIZE
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

    def go_down(self):
        next_x, next_y = self.xcor(), self.ycor() - TILESIZE
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

    def go_left(self):
        next_x, next_y = self.xcor() - TILESIZE, self.ycor()
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

    def go_right(self):
        next_x, next_y = self.xcor() + TILESIZE, self.ycor()
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

class Enemy(Sprite):
  
    def __init__(self, _x, _y):
        Sprite.__init__(self)
        self.shape(enemy)
        self.x = _x
        self.y = _y
        self.goto(self.x, self.y)
        self.direction = random.choice(["up", "down", "left", "right"])

    # Enemy Movement  
    def move(self):
        if self.direction == "up":
            next_x, next_y = self.xcor(), self.ycor() + TILESIZE
        elif self.direction == "down":
            next_x, next_y = self.xcor(), self.ycor() - TILESIZE
        elif self.direction == "left":
            next_x, next_y = self.xcor() - TILESIZE, self.ycor()
        elif self.direction == "right":
            next_x, next_y = self.xcor() + TILESIZE, self.ycor()
  
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
  
        # Reset timer  
        screen.ontimer(self.move, random.randint(100, 300))

class Wall(Sprite):
  
    def __init__(self):
        Sprite.__init__(self)
        self.shape(wall)
    
class Door(Sprite):
  
    def __init__(self, _x, _y):
        Sprite.__init__(self)
        self.shape(door_closed)
        self.x = _x
        self.y = _y
        self.goto(self.x, self.y)

class Chest(Sprite):
  
    def __init__(self, _x, _y):
        Sprite.__init__(self)
        self.shape(chest)
        self.goto(_x, _y)
        self.gold = 100
    
  
class Key(Sprite):
  
    def __init__(self, _x, _y):
        Sprite.__init__(self)
        self.shape(key)
        self.goto(_x, _y)
  
levels = []
levels.append(maze_map_0)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the mumber of every item in the mace
            item_number = level[y][x]
            # Berechne die Bildschirmkoordinaten
            screen_x = -192 + (x*TILESIZE)
            screen_y =  192 - (y*TILESIZE)
      
            # Prüfe, ob Item ein Wall ist
            if item_number == WALL:
                wall.goto(screen_x, screen_y)
                wall.stamp()
                walls.append((screen_x, screen_y))
        
            # Prüfe, ob Item eine Tür ist
            if item_number == DOOR:
                door = Door(screen_x, screen_y)
                doors.append(door)
                walls.append((door.x, door.y))

            # Prüfe, ob Item der Spieler ist
            if item_number == PLAYER:
                player.start_x = screen_x
                player.start_y = screen_y
                player.goto(screen_x, screen_y)
        
            # Prüfe, ob Item ein Enemy ist
            if item_number == ENEMY:
                enemy = Enemy(screen_x, screen_y)
                enemies.append(enemy)

            # Prüfe, ob Item eine Schatztrue ist
            if item_number == CHEST:
                chests.append(Chest(screen_x, screen_y))
        
            # Prüfe, ob Item eine Schlüssel ist
            if item_number == KEY:
                keys.append(Key(screen_x, screen_y))

wall = Wall()
walls = []
doors = []
chests = []
keys = []
player = Player()
enemies = []

# Level Setup
setup_maze(levels[0])
# print(enemies)

# Das Spiel beenden
def exit_game():
    global keep_going
    print("Bye, bye, Baby")
    keep_going = False

# Auf Tastaturereignisse lauschen
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

screen.onkey(exit_game, "q")   # Das Spiel beenden

# Spiel starten
print("🧙 Start Simple Maze Game Stage 3 🧙")

# Timer setzen
for enemy in enemies:
    screen.ontimer(enemy.move, random.randint(100, 300))

keep_going = True
while keep_going:
    # Hat der Spieler eine Schatzkiste gefunden?
    for chest in chests:
        if player.is_collision(chest):
            player.gold += chest.gold
            print("Player Gold: {}".format(player.gold))
            # Verberge die Schatzkiste
            chest.destroy()
            # Lösche die Schatzkiste aus der Liste
            chests.remove(chest)
    # Hat der Spieler einen Schlüssel gefunden?
    for key in keys:
        if player.is_collision(key):
            player.has_key = True
            for door in doors:
                door.shape(door_open)
                walls.remove((door.x, door.y))
            print("Spieler besitzt einen Schlüssel")
            # Verberge den Schlüssel
            key.destroy()
            # Lösche den Schlüssel aus der Liste
            keys.remove(key)
  
    # Kollidiert der Spieler mit einem Gegner?
    for enemy in enemies:
        if player.is_collision(enemy):
            player.goto(player.start_x, player.start_y)
            print("Player stirbt!")
  
    # Ist der Spieler dem Labyrint entkommen?
    if player.xcor() >= 192:
        player.goto(player.xcor() - TILESIZE, player.ycor())
        print("**Gewonnen!**")
        exit_game()
    
    screen.update()   # den gesamten Bildschirm neu zeichnen
  
