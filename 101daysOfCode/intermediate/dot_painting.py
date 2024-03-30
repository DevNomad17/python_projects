from colorgram import *
from turtle import Turtle, Screen
import random


def dot(diameter):
    current_color = random.choice(colors)
    current_color_rgb = (current_color.rgb.r / 255, current_color.rgb.g / 255, current_color.rgb.b / 255)
    # print(current_color.rgb)
    brush.pencolor(current_color_rgb)
    brush.fillcolor(current_color_rgb)
    brush.begin_fill()
    brush.circle(diameter)
    brush.end_fill()


def line_of_dots(number, diameter):
    for _ in range(number):
        dot(diameter)
        brush.penup()
        brush.forward(diameter*4)
        brush.pendown()


def set_starting_position():
    brush.penup()
    brush.setpos(-screen.window_width()/3, screen.window_height()/3)
    brush.pendown()


def next_line(diameter):
    brush.penup()
    brush.setpos(-screen.window_width()/3, brush.ycor() - diameter*4)
    brush.pendown()


def paint_hirst(number_of_dots, diameter):
    set_starting_position()
    for _ in range(number_of_dots):
        line_of_dots(number_of_dots, diameter)
        next_line(diameter)


screen = Screen()

colors = colorgram.extract('hirst.jpg',15)
brush = Turtle()
brush.speed("fastest")

paint_hirst(20, 10)
brush.hideturtle()

screen.exitonclick()
