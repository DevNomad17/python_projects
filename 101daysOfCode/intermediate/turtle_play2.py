import random
from turtle import Turtle, Screen


def square(size):
    for _ in range(4):
        timmy.forward(size)
        timmy.right(90)


def dash_line(length):
    for _ in range(int(length/10)):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def color_randomizer():
    timmy.pencolor(random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)


def polygons(length):
    for i in range(3, 10):
        color_randomizer()
        for _ in range(i):
            timmy.right(360/i)
            timmy.forward(length)


def random_walk(pace_length):
    timmy.width(5)
    timmy.speed("fastest")
    while True:
        color_randomizer()
        timmy.right(random.randint(0, 4)*90)
        timmy.forward(pace_length)


# def circle(diameter):
#     color_randomizer()
#     for _ in range(90):
#         timmy.right(4)
#         timmy.forward(diameter/20)


def spiro(thickness):
    for _ in range(int(thickness)):
        color_randomizer()
        timmy.circle(100)
        timmy.right(360/thickness)


timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
# square(200)
# dash_line(300)
# polygons(100)
# random_walk(10)
spiro(90)
screen = Screen()
screen.exitonclick()
