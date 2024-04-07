from turtle import Screen
from pong_scoreboard import Scoreboard
from pong_paddle import Paddle

from pong_settings import SCREEN_HEIGHT, SCREEN_WIDTH


def setup_screen():
    s = Screen()
    s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    s.bgcolor("black")
    s.title("Pong")
    s.tracer(0)
    return s


screen = setup_screen()
p1 = Paddle(1)
p2 = Paddle(2)
score_p1 = Scoreboard(1)
score_p2 = Scoreboard(2)
screen.update()


# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")


# game_is_on = True
# while game_is_on:
#     snake.move()
#     if not snake.moving:
#         snake.hide()
#         scoreboard.game_over()
#         break
#     screen.update()
#     time.sleep(DELAY)
#
#     if snake.head.distance(food) < OFFSET_SEGMENT / 1.3:
#         food.refresh()
#         snake.grow()
#         scoreboard.increase()

screen.exitonclick()
