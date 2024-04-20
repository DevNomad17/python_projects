from turtle import Turtle
from pong_settings import PADDLE_SIZE, SCREEN_WIDTH, OFFSET_SEGMENT, OFFSET_LEFT_EDGE, DOWN, UP, \
    UPPER_EDGE, LOWER_EDGE


def create_segment():
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    return segment


class Paddle:
    def __init__(self, player_no):
        self.body = []
        self.moving = False
        self.heading = 0
        for segment in range(PADDLE_SIZE):
            segment = create_segment()
            if player_no == 1:
                x = SCREEN_WIDTH / -2 + OFFSET_LEFT_EDGE / 2
                y = segment.ycor() + (PADDLE_SIZE / 2 - len(self.body)) * OFFSET_SEGMENT
                segment.setpos(x, y)
            else:
                x = SCREEN_WIDTH / 2 - OFFSET_SEGMENT
                y = segment.ycor() + (PADDLE_SIZE / 2 - len(self.body)) * OFFSET_SEGMENT
                segment.setpos(x, y)
            self.body.append(segment)

    def up(self):
        if self.moving:
            if self.heading == DOWN:
                self.moving = False
        else:
            self.heading = UP
            self.moving = True

    def down(self):
        if self.moving:
            if self.heading == UP:
                self.moving = False
        else:
            self.heading = DOWN
            self.moving = True

    def reverse(self):
        if self.heading == UP:
            self.heading = DOWN
        else:
            self.heading = UP

    def move(self):
        if self.moving:
            if self.body[0].ycor() >= UPPER_EDGE and self.heading == UP:
                self.reverse()
            elif self.body[-1].ycor() <= LOWER_EDGE and self.heading == DOWN:
                self.reverse()
            else:
                for segment in self.body:
                    segment.setheading(self.heading)
                    segment.forward(OFFSET_SEGMENT)

    def ycor_min(self):
        y_min = UPPER_EDGE
        for segment in self.body:
            if segment.ycor() < y_min:
                y_min = segment.ycor()
        return y_min - OFFSET_SEGMENT

    def ycor_max(self):
        y_max = LOWER_EDGE
        for segment in self.body:
            if segment.ycor() > y_max:
                y_max = segment.ycor()
        return y_max + OFFSET_SEGMENT
