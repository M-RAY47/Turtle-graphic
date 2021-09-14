from turtle import Turtle, Screen, title
import random as rd

title("Turtle Race")
screen = Screen()
screen.setup(width=500, height=400)
y_axis = [-100, -65, -30, +5, +35, +70, +105]
colors = ['green', 'blue', 'yellow', 'red', 'purple', 'orange', 'violet']
user_bet = screen.textinput(title="Bet your winner", prompt="Which turtle will win the race? Enter a color: ")
referee = Turtle(shape='turtle')
referee.color("black"); referee.penup()
referee.goto(x=+235, y=-115); referee.pendown()
referee.setheading(90); referee.speed('fast')

all_turtles =[]
def race():
	referee.fd(245)
	for i in range(0,7):
		new_turtle = Turtle(shape='turtle')
		new_turtle.color(colors[i])
		new_turtle.penup()
		new_turtle.goto(x=-230, y=y_axis[i])
		all_turtles.append(new_turtle)
	return all_turtles

if user_bet:
	start_race = True
	race()

while start_race:
	if referee.ycor() == +130.00:
		for turtle in all_turtles:
			if turtle.xcor() > 215:
				start_race = False
				winning_color = turtle.pencolor()
				if winning_color == user_bet:
					results = screen.textinput(title="Result", prompt=f"You have won! The {winning_color} turtle is the winner!!!")
				else:
					results = screen.textinput(title="Result", prompt=f"You have lost! The {winning_color} turtle is the winner!!!")
				
			move = rd.randint(0, 10)
			turtle.fd(move)





screen.exitonclick()
