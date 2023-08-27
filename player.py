import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
turtle.register_shape("squirtle.gif")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("squirtle.gif")
        self.setheading(90)
        self.set_turtle()


    def set_turtle(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def on_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

