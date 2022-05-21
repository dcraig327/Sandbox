import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.HIGH_SCORE_FILENAME = "data.txt"
        self.score = 0
        self.high_score = self.score
        with open(self.HIGH_SCORE_FILENAME, "a+") as file:
            if not file.tell():
                file.write("0")
            file.seek(0)
            self.high_score = int(file.read())
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.redraw()

    def draw(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 22, 'normal'))

    def redraw(self):
        self.clear()
        self.draw()

    def increase(self):
        self.score += 1
        self.redraw()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.HIGH_SCORE_FILENAME, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.redraw()

    #
    # def game_over(self):
    #     self.goto(0, -50)
    #     self.write("   GAME OVER\n\nPress ESC to exit", align="center", font=('Courier', 22, 'normal'))
