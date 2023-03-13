# juggling_ball.py
import random
import turtle
class Ball(turtle.Turtle):
    """Create balls to use for juggling"""
    max_velocity = 5
    gravity = 0.07
    bat_velocity_change = 8
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.color(
            random.random(),
            random.random(),
            random.random(),
        )
        self.penup()
        self.setposition(
            random.randint(
                (-self.width // 2) + 20,
                (self.width // 2) - 20
            ),
            random.randint(
                (-self.height // 2) + 20,
                (self.height // 2) - 20
            ),
        )
        self.setheading(90)
        self.velocity = random.randint(1, self.max_velocity)
    def __repr__(self):
        return f"{type(self).__name__}({self.width}, {self.height})"
    def move(self):
        """Move the ball forward by the amount required in a frame"""
        self.forward(self.velocity)
        self.fall()
    def fall(self):
        """Take the effect of gravity into account"""
        self.velocity -= self.gravity
    def is_below_lower_edge(self):
        """
        Check is object fell through the bottom
        :return: True if object fell through the bottom.
                 False if object is still above the bottom edge
        """
        if self.ycor() < -self.height // 2:
            self.hideturtle()
            return True
        return False
    def bat_up(self):
        """Bat the ball upwards by increasing its velocity"""
        self.velocity += self.bat_velocity_change