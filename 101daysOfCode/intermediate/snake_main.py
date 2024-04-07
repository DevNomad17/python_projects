import time
from turtle import Screen
from snake_class import Snake
from snake_settings import DELAY, OFFSET_SEGMENT, SCREEN_HEIGHT, SCREEN_WIDTH
from snake_food import Food
from snake_score import Scoreboard


def setup_screen():
    s = Screen()
    s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    s.bgcolor("black")
    s.title("Snake")
    s.tracer(0)
    return s


screen = setup_screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    snake.move()
    if not snake.moving:
        snake.hide()
        scoreboard.game_over()
        break
    screen.update()
    time.sleep(DELAY)

    if snake.head.distance(food) < OFFSET_SEGMENT / 1.3:
        food.refresh()
        snake.grow()
        scoreboard.increase()

screen.exitonclick()
