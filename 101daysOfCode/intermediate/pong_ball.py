from turtle import Turtle
from pong_settings import OFFSET_SEGMENT, UPPER_EDGE, LOWER_EDGE, RIGHT_EDGE, LEFT_EDGE
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0, 359))

    def move(self):
        if self.ycor() >= UPPER_EDGE or self.ycor() <= LOWER_EDGE:
            self.setheading(360 - self.heading())
        if self.xcor() >= RIGHT_EDGE or self.xcor() <= LEFT_EDGE:
            self.setheading(180 - self.heading())
        self.forward(OFFSET_SEGMENT)