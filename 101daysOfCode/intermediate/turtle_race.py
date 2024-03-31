import random
from turtle import Turtle, Screen


racers = []
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange', 'brown', 'purple', 'grey']
SCREEN_EDGE_OFFSET = 30
RACER_OFFSET = 40
PACE_VARIABILITY = 20


def starting_position(number_of_racers):
    for i in range(number_of_racers):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.setpos(x=screen.window_width() / -2 + SCREEN_EDGE_OFFSET, y=(number_of_racers / 2 - i) * RACER_OFFSET)
        racers.append(turtle)


def race_on():
    furthest = screen.window_width() / -2
    winning_color = colors[0]
    while furthest < screen.window_width() / 2 - SCREEN_EDGE_OFFSET:
        for turtle in racers:
            turtle.forward(random.randint(1, PACE_VARIABILITY))
            if turtle.xcor() > furthest:
                furthest = turtle.xcor()
                winning_color = turtle.color()[0]
    return winning_color


screen = Screen()
screen.setup(width=800, height=600)

starting_position(9)
bet = screen.textinput(title='Place your bet', prompt='Which turtle will win the race? Enter the color:')
winner = race_on()

if bet == winner:
    print(f"You've WON! The winner is {winner}")
else:
    print(f"You've lost! The winner is {winner}")

screen.bye()
