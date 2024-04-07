from turtle import Turtle
from pong_settings import PADDLE_SIZE, SCREEN_WIDTH, OFFSET_SEGMENT, OFFSET_LEFT_EDGE


def create_segment():
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    return segment


class Paddle:
    def __init__(self, player_no):
        self.body = []
        for segment in range(PADDLE_SIZE):
            segment = create_segment()
            if player_no == 1:
                segment.setpos(SCREEN_WIDTH / -2 + OFFSET_LEFT_EDGE / 2, segment.ycor() + (PADDLE_SIZE / 2 - len(self.body)) * OFFSET_SEGMENT)
            else:
                segment.setpos(SCREEN_WIDTH / 2 - OFFSET_SEGMENT, segment.ycor() + (PADDLE_SIZE / 2 - len(self.body)) * OFFSET_SEGMENT)
            self.body.append(segment)


