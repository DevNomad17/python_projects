from turtle import Turtle
from snake_settings import OFFSET_SEGMENT, SCREEN_HEIGHT
import time
from pathlib import Path

FILE_PATH = "snake_highest_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setpos(-1.5 * OFFSET_SEGMENT, SCREEN_HEIGHT / 2 - OFFSET_SEGMENT)
        self.highest_score = 0
        if Path(FILE_PATH).exists():
            with open(FILE_PATH, "r") as file:
                score = int(file.read())
                if isinstance(score, int):
                    self.highest_score = score

        self.update_score()

    def update_score(self):
        self.clear()
        self.setpos(-1.5 * OFFSET_SEGMENT, SCREEN_HEIGHT / 2 - OFFSET_SEGMENT)
        self.write(arg=f"Score: {self.score} | Highest score: {self.highest_score}", align="center", font=("Courier", 12, "normal"))

    def increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        self.game_over()
        time.sleep(3)
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(FILE_PATH, "w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER! Final score: {self.score}", align="center", font=("Courier", 13, "normal"))
