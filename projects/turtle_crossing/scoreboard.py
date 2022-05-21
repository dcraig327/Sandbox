import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.FONT = ("Courier", 24, "normal")
        self.goto(-280, 240)

        self.score = 0
        self.draw()

    def draw(self):
        self.write(f"Level: {self.score}", align="left", font=self.FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.draw()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=self.FONT)
