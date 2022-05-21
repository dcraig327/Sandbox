import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")

    def draw(self):
        self.goto(-26 * 5, 108)
        self.write(f"{self.player1_score}", align="left", font=('wendy', 105, 'normal'))
        self.goto(26 * 6, 108)
        self.write(f"{self.player2_score}", align="left", font=('wendy', 105, 'normal'))

        # self.goto(-75, 165)
        # self.write(f"{self.player1_score}", align="left", font=('wendy', 57, 'bold'))
        # x = 0
        # if self.player2_score == 1:
        #     x = -2
        # elif self.player2_score < 10:
        #     x = -17
        # elif self.player2_score == 11:
        #     x = -26
        # elif self.player2_score < 20:
        #     x = -41
        # else:
        #     x = -48
        # self.goto(91, 165)

    def redraw(self):
        self.clear()
        self.draw()
