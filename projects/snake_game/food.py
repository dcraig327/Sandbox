import turtle
import random

DIAMETER = 20

WIDTH = 600
HEIGHT = 600


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
      #  self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        random.seed()
        self.refresh()

    def refresh(self):
        x = DIAMETER * random.randint(-14, 14)
        y = DIAMETER * random.randint(-14, 14)
        self.goto(x, y)

