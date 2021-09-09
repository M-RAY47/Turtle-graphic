from turtle import Turtle, Screen, pensize, title
import random as rd

title("Random walk")
screen = Screen()
screen.bgcolor("white")
milo = Turtle()
milo.heading()
milo.speed(1)
directions = [0, 90, 180, 270]
colors = ["CornflowerBlue", 'green', 'red', 'wheat', 'yellow', 'violet', "orange"]
milo.shape('turtle')
milo.pensize(width=15)


for i in range(100):
	milo.fd(30)
	milo.color(rd.choice(colors))
	milo.setheading(rd.choice(directions))



screen.exitonclick()