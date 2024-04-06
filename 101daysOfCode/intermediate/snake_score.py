from turtle import Turtle
from snake_settings import OFFSET_SEGMENT, SCREEN_HEIGHT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setpos(-OFFSET_SEGMENT, SCREEN_HEIGHT / 2 - OFFSET_SEGMENT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    def increase(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER! Final score: {self.score}", align="center", font=("Courier", 13, "normal"))
