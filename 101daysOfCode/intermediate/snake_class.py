from turtle import Turtle
from snake_settings import OFFSET_SEGMENT, DOWN, UP, LEFT, RIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, OFFSET_DIVIDER_CONSTANT


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
        self.moving = True

    def grow(self):
        s = create_segment()
        self.segments.append(s)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            if self.segments[i].distance(self.head) < (OFFSET_SEGMENT / OFFSET_DIVIDER_CONSTANT):
                self.moving = False
                return
            self.segments[i].setpos(self.segments[i - 1].pos())
        if abs(abs(self.head.xcor()) - SCREEN_WIDTH / 2) < OFFSET_SEGMENT:
            if self.isMovingHorizontally():
                self.head.setpos(-self.head.xcor(), self.head.ycor())
        elif abs(abs(self.head.ycor()) - SCREEN_HEIGHT / 2) < OFFSET_SEGMENT:
            if not self.isMovingHorizontally():
                self.head.setpos(self.head.xcor(), -self.head.ycor())
        self.head.forward(OFFSET_SEGMENT)

    def isMovingHorizontally(self):
        if self.head.heading() in (0, 180):
            return True
        else:
            return False

    def hide(self):
        for i in self.segments:
            i.hideturtle()

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


