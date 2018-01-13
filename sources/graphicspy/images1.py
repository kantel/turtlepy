import graphics as g
import os

WIDTH = 640
HEIGHT = 160


def main():
    win = g.GraphWin("Hildegund von Müthenmätz", WIDTH, HEIGHT)
    win.setBackground(g.color_rgb(200, 200, 200))

    path = os.path.join(os.getcwd(), "sources/graphics/images/hildegund.gif")
    hildegund = g.Image(g.Point(WIDTH-16, HEIGHT/2), path)
    hildegund.draw(win)
    
    dx = -1
    while True:
        hildegund.move(dx, 0)
        if hildegund.getAnchor().getX() <= 16 or hildegund.getAnchor().getX() >= WIDTH-16:
            dx *= -1

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

if __name__ == "__main__":
    main()