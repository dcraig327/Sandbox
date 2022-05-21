# never do this:
# from turtle import *

# if using it once or twice:
# import turtle
# tim = turtle.Turtle()

# you can create a module alias
# import turtle as t

# if using three or more:
import turtle
from turtle import Turtle, Screen
import heroes
import random

turtle.colormode(255)

screen = Screen()
screen.bgcolor((32, 32, 32))

tim = Turtle()
tim.shape("classic")
tim.color("blue1")


def turtle_circle():
    for _ in range(0, 4):
        tim.right(90)
        tim.forward(100)


# 10 line, 10 empty, repeat 50x
def turtle_dashed():
    for _ in range(0, 50):
        tim.pendown()
        tim.forward(3)
        tim.penup()
        tim.forward(3)


def turtle_shape(num_sides, color):
    angle = 360 / num_sides
    tim.color(color)
    for _ in range(0, num_sides):
        tim.right(angle)
        tim.forward(100)


colors = ["blue", "orange", "yellow", "red", "white", "green", "pink", "purple"]


def turtle_draw_shapes():
    for x in range(3, 11):
        turtle_shape(x, random.choice(colors))


def turtle_north():
    tim.setheading(0)


def turtle_south():
    tim.setheading(180)


def turtle_west():
    tim.setheading(270)


def turtle_east():
    tim.setheading(90)


def turtle_random_walk():
    direction = [turtle_north, turtle_east, turtle_south, turtle_west]
    random.choice(direction)()
    #    tim.color(random.choice(colors))
    tim.color(turtle_random_color())
    tim.forward(20)


def turtle_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def turtle_spirograph(circles):
    # draw 100 radius circle
    # try 100 circles
    for _ in range(0, circles):
        tim.color(turtle_random_color())
        tim.left(360 / circles)
        tim.circle(100)


random.seed()
tim.speed(0)
# screen.tracer(0)
screen.delay(1)
turtle_spirograph(65)
# screen.update()

# tim.width(10)
# while True:
#   screen.tracer(0)
#    turtle_random_walk()
#    screen.update()
# tim.width()

screen.exitonclick()
