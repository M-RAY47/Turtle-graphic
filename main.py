from turtle import Turtle, Screen
import random as rd

milo = Turtle()
milo.heading()
milo.speed(3)
colors = ["CornflowerBlue", 'green', 'red', 'wheat', 'yellow', 'violet', "orange"]
def make_fig(side_fig):
	angle = 360/side_fig
	for i in range(side_fig):
		milo.fd(100); milo.dot(10, rd.choice(colors))
		milo.rt(angle)

for i in range(3,11):
	milo.shape('turtle')
	milo.color(rd.choice(colors))
	make_fig(i)




screen = Screen()
screen.exitonclick()