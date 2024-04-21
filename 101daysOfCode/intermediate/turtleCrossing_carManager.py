import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SIZE = 2
OFFSET_SEGMENT = 20
CAR_DENSITY = 5


def create_segment(color_index):
    segment = Turtle()
    segment.shape("square")
    segment.color(COLORS[color_index])
    segment.penup()
    segment.setheading(180)
    return segment


class Car:
    def __init__(self):
        self.body = []
        color = random.randint(0, 5)
        y = random.randint(-280, 280)
        for segment in range(CAR_SIZE):
            segment = create_segment(color)
            x = 300 - len(self.body) * OFFSET_SEGMENT
            segment.setpos(x, y)
            self.body.append(segment)

    def moveForward(self, distance):
        for segment in self.body:
            segment.forward(distance)

    def getFront(self):
        return self.body[-1]

    def hideCar(self):
        for segment in self.body:
            segment.hideturtle()


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_increment = MOVE_INCREMENT

    def go(self, player):

        add_car = random.randint(0, 100) % CAR_DENSITY == 0
        if add_car:
            car = Car()
            self.cars.append(car)

        for car in self.cars:
            car.moveForward(self.move_increment)
            if player.distance(car.getFront()) < OFFSET_SEGMENT:
                return -1
            if car.getFront().xcor() < -280:
                car.hideCar()
                self.cars.pop(self.cars.index(car))

        return 1
