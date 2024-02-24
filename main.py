import pandas
import turtle

# import csv file:
state_data = pandas.read_csv("50_states.csv")
number_of_states = len(state_data["state"])
print(number_of_states)

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.bgpic(img)
turtle.Screen().setup(725, 491)
turtle.penup()

keep_going = True
guessed_states = []
while len(guessed_states) < number_of_states:
    answer = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State's name? ")).title()
    if answer not in guessed_states:
        guessed_states.append(answer)
        get_coordinates = state_data[state_data["state"] == answer.title()]
        x_cord = get_coordinates["x"].values[0]
        y_cord = get_coordinates["y"].values[0]
        turtle.teleport(x_cord, y_cord)
        turtle.pendown()
        turtle.write(answer)
        turtle.penup()
    else:
        pass
