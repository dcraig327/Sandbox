import colorgram
from turtle import Turtle, Screen
import random

random.seed()
screen = Screen()
screen.colormode(255)
screen.bgcolor((247, 245, 246))
t = Turtle()
t.speed(0)

# external padding: double size of internal padding
# internal padding: size of circle diameter
# circle diameter: 20

w = 12
h = 7
num_colors = w * h
colors = colorgram.extract('hirst.webp', num_colors)
d = 30
r = d / 2


def draw_circle():
    c = random.choice(colors).rgb
    t.color(c, c)
    #    t.fillcolor(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def draw_circles():
    t.penup()
    # t.setposition(-r * w, r * h)
    t.goto(-1 * w * d, 0)
    t.pendown()
    for y in range(0, h):
        t.penup()
        t.goto(-1 * w * d, -d * 2 * y)
        for x in range(0, w):
            draw_circle()
            t.penup()
            t.setheading(0)
            t.forward(d * 2)
            t.pendown()


draw_circles()

screen.exitonclick()
