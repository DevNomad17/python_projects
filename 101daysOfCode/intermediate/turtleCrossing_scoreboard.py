from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setpos(-200, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER!", align="center", font=FONT)
