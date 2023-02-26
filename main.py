import turtle
import pandas
from correct import Name

name=Name()

screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data=pandas.read_csv("50_states.csv")
correct_guess=0
coords=state_data[["x","y"]]
correct_guesses=[]
end=False

while correct_guess<50 and end==False:
    answer_state = screen.textinput(title=f"{correct_guess}/50 States Correct",prompt="What's another state name?")
    n=-1
    if answer_state.lower()=="exit":
        states_to_learn = []
        for state in state_data["state"]:
            if state not in correct_guesses:
                states_to_learn.append(state)

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("to_learn")
        end=True

    for state_name in state_data["state"]:
        n += 1
        if state_name.lower()==answer_state.lower() and answer_state not in correct_guesses:
            correct_guesses.append(state_name)
            correct_guess+=1
            coord=coords.loc[n]
            name.write_state(state_name= state_name,cors=coord)










