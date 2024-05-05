from turtle import Turtle, Screen
import pandas
import turtle

IMAGE = "blank_states_img.gif"
DATA_FILE = "50_states.csv"
RESULT_FILE = "missed_states.txt"


def missing_states(all_states, guessed_states):
    return list(set(all_states) - set(guessed_states))


screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states_data = pandas.read_csv(DATA_FILE)
score = 0
guessed_states_list = []

while True:
    title = "Guess the State"
    prompt = "Type the name of the state that is not revealed yet"
    answer_state = screen.textinput(title=f"{title} | Current score: {score}/50", prompt=prompt).title()
    if answer_state == 'Exit':
        with open(RESULT_FILE, "w") as file:
            for item in missing_states(states_data.state.to_list(), guessed_states_list):
                file.write(str(item) + '\n')
        break
    answer_state_data = states_data[states_data.state == answer_state]
    # split = states_data[states_data.state == answer_state].values[0]
    # print(split[0])
    if not answer_state_data.empty:
        state = answer_state_data.state.item()
        x_cor = answer_state_data.x.item()
        y_cor = answer_state_data.y.item()
        if state not in guessed_states_list:
            guessed_states_list.append(state)
            state_name = Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.setpos(x_cor, y_cor)
            state_name.write(arg=state, align="center", font=("Courier", 8, "normal"))
            score += 1
            if score == 50:
                print("Congrats, you've won!!!")
                break
            # print(state)
print("Bye bye")
turtle.mainloop()
