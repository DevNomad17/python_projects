import random
from turtle import Turtle
from snake_settings import OFFSET_SEGMENT, SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-SCREEN_WIDTH / 2 + OFFSET_SEGMENT, SCREEN_WIDTH / 2 - OFFSET_SEGMENT)
        y = random.randint(-SCREEN_HEIGHT / 2 + OFFSET_SEGMENT, SCREEN_HEIGHT / 2 - OFFSET_SEGMENT)
        self.setpos(x, y)
