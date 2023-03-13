# juggling_balls_game.py

import turtle
import time
import random

from juggling_ball import Ball

# Game parameters
WIDTH = 600
HEIGHT = 600

frame_rate = 30
batting_tolerance = 40
spawn_interval_range = (1, 5)
balls_lost_limit = 10

# Setup window
window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.bgcolor(0.15, 0.15, 0.15)
window.tracer(0)

# Batting function
def click_ball(x, y):
    for ball in balls:
        if ball.distance(x, y) < batting_tolerance:
            ball.bat_up()

window.onclick(click_ball)

balls = []

# Game loop
game_timer = time.time()
spawn_timer = time.time()
spawn_interval = 0
balls_lost = 0
while balls_lost < balls_lost_limit:
    frame_start_time = time.time()
    # Spawn new ball
    if time.time() - spawn_timer > spawn_interval:
        balls.append(Ball(WIDTH, HEIGHT))
        spawn_interval = random.randint(*spawn_interval_range)
        spawn_timer = time.time()

    # Move balls
    for ball in balls:
        ball.move()
        if ball.is_below_lower_edge():
            window.update()
            balls.remove(ball)
            turtle.turtles().remove(ball)
            balls_lost += 1

    # Update window title
    window.title(
        f"Time: {time.time() - game_timer:3.1f} | Balls lost: {balls_lost}"
    )

    # Refresh screen
    window.update()

    # Control frame rate
    loop_time = time.time() - frame_start_time
    if loop_time < 1 / frame_rate:
        time.sleep(1 / frame_rate - loop_time)

# Game over
final_time = time.time() - game_timer
# Hide balls
for ball in balls:
    ball.hideturtle()
window.update()
# Show game over text
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.write(
    f"Game Over | Time taken: {final_time:2.1f}",
    align="center",
    font=("Courier", 20, "normal")
)
turtle.done()