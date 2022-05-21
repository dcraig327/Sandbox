import turtle


class Fps(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.fps = 0
        self.color("gray")
        self.BOARD_TOP = 261
        self.BOARD_BOTTOM = -254
        self.BOARD_LEFT = -427
        self.BOARD_RIGHT = 421

    def draw(self):
        self.goto(self.BOARD_LEFT+1, self.BOARD_TOP-15)
        self.write(f"{self.fps}", align="left", font=('wendy', 12, 'normal'))

    def redraw(self):
        self.clear()
        self.draw()
