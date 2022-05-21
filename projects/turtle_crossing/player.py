import turtle


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()

        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10  # move on each update

        self.start()

    def start(self):
        self.clear()
        self.setheading(90)
        self.goto(self.STARTING_POSITION)

    def move(self):
        self.forward(self.MOVE_DISTANCE)
