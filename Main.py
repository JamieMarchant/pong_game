from turtle import Screen
from paddle_classes import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen Settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# class creation
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# key inputs for both paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        

    # Check collison with right and left paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        

    # check for Collison with right border
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()
    
    # check for collison with left border
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()
        
# close game on click
screen.exitonclick()
