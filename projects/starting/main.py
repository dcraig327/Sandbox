# never do this:
# from turtle import *

# if using it once or twice:
# import turtle
# tim = tutrle.Turtle()

# you can create a module alias
# import turle as t

# if using three or more:
from turtle import Turtle, Screen

# import heroes

# print(heroes.gen())

tim = Turtle()
tim.shape("classic")
tim.color("blue1")

# for _ in range(0, 4):
#     tim.right(90)
#     tim.forward(100)

screen = Screen()
screen.bgcolor("black")

screen.exitonclick()
