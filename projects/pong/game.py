import turtle
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle1, Paddle2
from net import Net
from fps import Fps
import time


# TODO: get a real engine
# TODO: add mouse handler
# TODO: add real keyboard handler

# there is no game over screen
# it goes to the demo of the game, but keeps the last score of the last game

# ai has max velocity moving the paddle, but precise with hitting the ball

# ai's max veocity depends on player skill, ai will save it's interactions with player
# 1 sound hitting paddle or wall
# 1 sound hitting left/right edge
# collision logic in game class


class Game:
    WINDOW_TITLE = "Pong"
    WINDOW_BG_COLOR = "black"
    WIDTH = 858
    HEIGHT = 525
    TICK_MS_DELAY = 16.5

    BOARD_TOP = 261
    BOARD_BOTTOM = -254
    BOARD_LEFT = -427
    BOARD_RIGHT = 421

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=self.WIDTH, height=self.HEIGHT, startx=None, starty=250)
        self.screen.getcanvas().winfo_toplevel().resizable(False, False)
        self.screen.title(self.WINDOW_TITLE)
        self.screen.bgcolor(self.WINDOW_BG_COLOR)
        self.screen.delay(0)
        self.screen.tracer(0, 0)

        self.scoreboard = Scoreboard()
        self.fps = Fps()
        self.last_time = 0
        self.net = Net()
        self.paddle1 = Paddle1()
        self.paddle2 = Paddle2()
        self.ball = Ball()

        self.tick_ms_delay = self.TICK_MS_DELAY

        self.game_active = True
        self.start_game()

        self.screen.listen()
        self.screen.onkeypress(self.paddle_up, "w")
        self.screen.onkeypress(self.paddle_down, "s")
        self.screen.onkeypress(self.paddle_up, "Up")
        self.screen.onkeypress(self.paddle_down, "Down")
        self.screen.onkey(self.end_game, "Escape")
        self.screen.mainloop()

    # d = (1/(() / 1000000.0))
    # self.fps = d
    def sync(self):
        delta = 0
        t = 0
        ns_delay = self.tick_ms_delay * 1000000
        while delta < ns_delay:
            t = time.time_ns()
            delta = t - self.last_time
        self.fps.fps = int(round((1.0 / delta) * 1000000000, 0))

        self.last_time = t

    def physics(self):
        if self.ball.x < self.BOARD_LEFT - 9:
            self.ball.die()
            self.scoreboard.player2_score += 1
            self.scoreboard.redraw()
            self.ball.birth()
        elif self.ball.x > self.BOARD_RIGHT:
            self.ball.die()
            self.scoreboard.player1_score += 1
            self.scoreboard.redraw()
            self.ball.birth()
        if self.ball.y < self.BOARD_BOTTOM + 9:
            self.ball.y = self.BOARD_BOTTOM + 9
            self.ball.dy = 1
        elif self.ball.y > self.BOARD_TOP:
            self.ball.y = self.BOARD_TOP
            self.ball.dy = -1
        if self.ball.xcor() < (self.paddle1.xcor() + self.paddle1.PADDLE_WIDTH):
            if (self.ball.ycor() - self.ball.BALL_SIZE + 1) <= self.paddle1.ycor():
                if self.ball.ycor() >= (self.paddle1.ycor() - self.paddle1.PADDLE_HEIGHT):
                    self.ball.dx = 1
                    self.ball.x = (self.paddle1.xcor() + self.paddle1.PADDLE_WIDTH)
        elif self.ball.xcor() > (self.paddle2.xcor() - self.ball.BALL_SIZE):
            self.ball.x = self.paddle2.xcor() - self.ball.BALL_SIZE
            self.ball.dx = -1

    # TODO: paddle2 collision
    # TODO: paddl1 and paddle2 top/bottom collision
    # TODO: move paddle with mouse

    def update(self):
        self.sync()
        self.ball.move()
        self.physics()

    def render(self):
        self.paddle1.redraw()
        self.paddle2.redraw()
        self.ball.redraw()
        self.fps.redraw()

    def tick(self):
        while self.game_active:
            self.update()
            self.render()

    def start_game(self):
        self.scoreboard.draw()
        self.net.draw()
        # draw paddles
        self.paddle1.draw()
        self.paddle2.draw()
        # draw ball
        self.ball.draw()
        # if we draw a wall, at bottom under the wall, show ESC to exit game
        # if not playing
        # have two paddles automatically move
        # have ball auto move
        # have logic auto work
        # have score not work
        # show score from the score object
        # show somewhere on the board, press ESC to exit, LMB to start game
        self.fps.draw()
        turtle.ontimer(self.tick, 17)

    def paddle_up(self):
        self.paddle1.y += 10

    def paddle_down(self):
        self.paddle1.y -= 10

    def player1_scores(self):
        self.scoreboard.player1_score += 1
        self.scoreboard.redraw()

    def player2_scores(self):
        self.scoreboard.player2_score += 1
        self.scoreboard.redraw()

    def end_game(self):
        self.game_active = False
        self.screen.onkey(exit, "Escape")

# mouse will control paddle
# LMB will start game
# ESC will end game and go back to title screen
# at title screen ESC will close game

# title screen is created by game class
# the game screen is created by game class


# def game_over(self):
#     self.goto(0, 0)
#     self.write("   GAME OVER\n\nPress ESC to exit", align="center", font=('Courier', 22, 'normal'))


# boundries:
# self.x = self.BOARD_LEFT
# self.x = self.BOARD_RIGHT - 9
# self.y = self.BOARD_TOP
# self.y = self.BOARD_BOTTOM + 9
