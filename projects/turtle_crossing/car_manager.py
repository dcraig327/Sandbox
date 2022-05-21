import turtle
import random


class CarManager():
    def __init__(self):
        super().__init__()
        random.seed()

        self.COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.STARTING_MOVE_DISTANCE = 5  # default move distance at lvl 0
        self.MOVE_INCREMENT = 10  # added to move distance on each level up
        self.SPAWN_Y_MAX = 230
        self.SPAWN_Y_MIN = -230
        self.SPAWN_X = 320
        self.CAR_HEIGHT = 21

        self.cars = []
        self.speed = self.STARTING_MOVE_DISTANCE

    def is_car_coming(self):
        if random.random() > 0.9:
            return True
        else:
            return False

    def spawn(self):
        t = turtle.Turtle("square")
        t.penup()
        t.shapesize(1, 2, None)
        t.color(random.choice(self.COLORS))
        t.setheading(180)
        t.goto(self.SPAWN_X, random.randrange(self.SPAWN_Y_MIN, self.SPAWN_Y_MAX))
        self.cars.append(t)

    def move(self):
        if self.is_car_coming():
            self.spawn()
        for car in self.cars:
            car.forward(self.speed)

    def increase(self):
        self.speed += self.MOVE_INCREMENT
