# Pong!
from turtle import Screen, Turtle

# Screen Settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

right_paddle = Turtle(shape="square")
right_paddle.penup()
right_paddle.color("white")
right_paddle.turtlesize(stretch_wid=5, stretch_len=1)
right_paddle.setpos(x=350, y=0)


def up():
    right_paddle.setheading(up)


screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.listen()


# close game on click
screen.exitonclick()