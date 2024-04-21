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
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    if car_manager.go(player) < 0:
        scoreboard.game_over()
        game_is_on = False
    screen.update()
    if player.isInFinish():
        scoreboard.increase()
        player.respawn()
        car_manager.move_increment += 5
    time.sleep(0.1)


screen.exitonclick()
