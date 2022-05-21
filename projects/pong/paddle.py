import turtle

#top,left is 0,0

# 25W, 70H paddle
# paddle has 5 areas
class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.PADDLE_WIDTH = 12
        self.PADDLE_HEIGHT = 34
        self.BOARD_TOP = 261
        self.BOARD_BOTTOM = -254
        self.BOARD_LEFT = -427
        self.BOARD_RIGHT = 421
        self.ANGLE_UP = 90
        self.ANGLE_LEFT = 180
        self.ANGLE_RIGHT = 0
        self.ANGLE_DOWN = 270
        self.shape("square")
        self.color("white")
        self.pensize(4)
        self.x = 0
        self.y = 0

    def draw(self):
        self.setheading(self.ANGLE_RIGHT)
        self.goto(self.x, self.y)
        self.begin_fill()
        for n in range(2):
            self.forward(12)
            self.right(90)
            self.forward(34)
            self.right(90)
        self.end_fill()

    def redraw(self):
        self.clear()
        self.draw()


class Paddle1(Paddle):
    def __init__(self):
        super().__init__()
        self.x = self.BOARD_LEFT + 35
 #       self.x = -10


class Paddle2(Paddle):
    def __init__(self):
        super().__init__()
        self.x = self.BOARD_RIGHT - 46
#434l
#r415