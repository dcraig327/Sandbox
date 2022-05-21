import turtle


# 6H separation between net-section
# 14W, 24H net-section
# WIDTH = 858
# HEIGHT = 525

class Net(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
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

    # pen starts at top-left of net-section
    def draw_net_section(self):
        self.begin_fill()
        for n in range(2):
            self.forward(6)
            self.right(90)
            self.forward(12)
            self.right(90)
        self.end_fill()

    def draw(self):
        self.setheading(self.ANGLE_RIGHT)
        for n in range(28):
            self.goto(-10, self.BOARD_TOP - (n * 18) - 10)
            self.draw_net_section()

    def redraw(self):
        self.clear()
        self.draw()
