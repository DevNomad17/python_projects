from turtle import Turtle
from pong_settings import OFFSET_SEGMENT, UPPER_EDGE, LOWER_EDGE, RIGHT_EDGE, LEFT_EDGE
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(random.randint(0, 359))

    def move(self, p_left, p_right):
        if self.ycor() >= UPPER_EDGE or self.ycor() <= LOWER_EDGE:
            self.setheading(360 - self.heading())

        if self.xcor() <= LEFT_EDGE + OFFSET_SEGMENT:
            if p_left.ycor_min() <= self.ycor() <= p_left.ycor_max():
                self.setheading(180 - self.heading())

        if self.xcor() >= RIGHT_EDGE - OFFSET_SEGMENT:
            if p_right.ycor_min() <= self.ycor() <= p_right.ycor_max():
                self.setheading(180 - self.heading())

        self.forward(1.5*OFFSET_SEGMENT)