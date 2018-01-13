import graphics as g
import os

WIDTH = 640
HEIGHT = 320
STEP = 32

def main():
    win = g.GraphWin("Rogue 1", WIDTH, HEIGHT)
    win.setBackground(g.color_rgb(200, 200, 200))

    path1 = os.path.join(os.getcwd(), "sources/graphics/images/ground1.gif")
    bg = g.Image(g.Point(WIDTH/2, HEIGHT/2), path1)
    bg.draw(win)
    path2 = os.path.join(os.getcwd(), "sources/graphics/images/superhero.gif")
    rogue = g.Image(g.Point(WIDTH/2-STEP/2, HEIGHT/2-STEP/2), path2)
    rogue.draw(win)
    
    keepGoing = True
    while keepGoing:
        dx = dy = 0
        key = win.getKey()
        # print(key)
        if key == "Left":
            dx = -STEP
            if rogue.getAnchor().x == STEP/2:
                dx = 0
        elif key == "Right":
            dx = STEP
            if rogue.getAnchor().x == WIDTH-STEP/2:
                dx = 0
        elif key == "Up":
            dy = -STEP
            if rogue.getAnchor().y == STEP/2:
                dy = 0
        elif key == "Down":
            dy = STEP
            if rogue.getAnchor().y == HEIGHT-STEP/2:
                dy = 0
        elif key == "Escape":
            keepGoing = False
            
        print(rogue.getAnchor())
        rogue.move(dx, dy)

        

if __name__ == "__main__":
    main()