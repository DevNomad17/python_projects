import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SIZE = 2
OFFSET_SEGMENT = 20


def create_segment(color_index):
    segment = Turtle()
    segment.shape("square")
    segment.color(COLORS[color_index])
    segment.penup()
    return segment


class Car:
    def __init__(self):
        self.body = []
        self.heading = 180
        color = random.randint(0, 5)
        y = random.randint(-280, 280)
        for segment in range(CAR_SIZE):
            segment = create_segment(color)
            x = 300 - len(self.body) * OFFSET_SEGMENT
            segment.setpos(x, y)
            self.body.append(segment)


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        pass

