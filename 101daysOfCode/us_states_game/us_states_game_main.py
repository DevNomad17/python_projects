from turtle import Turtle, Screen
import pandas
import turtle


IMAGE = "blank_states_img.gif"
DATA_FILE = "50_states.csv"

screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states_data = pandas.read_csv(DATA_FILE)
score = 0


while True:
    title = "Guess the State"
    prompt = "Type the name of the state that is not revealed yet"
    answer_state = screen.textinput(title=f"{title} | Current score: {score}/50", prompt=prompt)
    answer_state_data = states_data[states_data.state == answer_state]
    if not answer_state_data.empty:
        answer_list = answer_state_data.to_dict('list')
        state_name = Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.setpos(answer_list['x'][0], answer_list['y'][0])
        state_name.write(arg=answer_list['state'][0], align="center", font=("Courier", 8, "normal"))
        score += 1
    else:
        break


turtle.mainloop()
