import time
from turtle import Screen
from turtleCrossing_player import Player
from turtleCrossing_carManager import CarManager
from turtleCrossing_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
