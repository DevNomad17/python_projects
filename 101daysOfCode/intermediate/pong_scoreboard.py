from turtle import Turtle
from pong_settings import OFFSET_SEGMENT, SCREEN_HEIGHT, PADDLE_SIZE, DOWN


def center_line():
    liner = Turtle()
    liner.speed("fastest")
    liner.color("white")
    liner.hideturtle()
    liner.penup()
    liner.setpos(liner.xcor(), SCREEN_HEIGHT / 2)
    liner.setheading(DOWN)
    i = 0
    while liner.ycor() > SCREEN_HEIGHT / -2:
        if i % 2 == 0:
            liner.pendown()
        else:
            liner.penup()
        liner.forward(OFFSET_SEGMENT)
        i += 1


class Scoreboard(Turtle):

    def __init__(self, player_no):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        if player_no == 1:
            self.setpos(-OFFSET_SEGMENT * PADDLE_SIZE, SCREEN_HEIGHT / 2 - PADDLE_SIZE * OFFSET_SEGMENT)
            center_line()
        else:
            self.setpos(OFFSET_SEGMENT * PADDLE_SIZE, SCREEN_HEIGHT / 2 - PADDLE_SIZE * OFFSET_SEGMENT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=("Courier", 40, "bold"))

    def increase(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER! Final score: {self.score}", align="center", font=("Courier", 13, "normal"))


