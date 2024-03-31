from turtle import Turtle, Screen


def move_forwards():
    brush.forward(10)


def move_backwards():
    brush.back(10)


def rotate_right():
    brush.right(5)


def rotate_left():
    brush.left(5)


def clear_screen():
    brush.setpos(0, 0)
    brush.clear()
    brush.setheading(0)


brush = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=rotate_left)
screen.onkey(key='d', fun=rotate_right)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
