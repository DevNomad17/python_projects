from turtle import Turtle
from snake_settings import OFFSET_SEGMENT, DOWN, UP, LEFT, RIGHT


def create_segment():
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    return segment


class Snake:
    def __init__(self):
        self.segments = []
        for _ in range(3):
            s = create_segment()
            s.setpos(-len(self.segments) * OFFSET_SEGMENT, 0)
            self.segments.append(s)
        self.head = self.segments[0]

    def grow(self):
        s = create_segment()
        self.segments.append(s)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.head.forward(OFFSET_SEGMENT)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)


