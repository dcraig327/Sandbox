import math
import turtle
import random


# top,left

# 21W, 21H ball
# ball x velocity is constant
# ball y velocity depends on where it hit the paddle
# after 12 hits it gets faster or changes angle, if you bounce straight across


# 2.09s paddle to paddle in a straight line
# 2.01s paddle to paddle bouncing on 2 walls

# uncertain:
# ball starts 50/50 on one side about 6px on either side
# spawns in a random y location up-along the net
# goes 45 deg towards the closest wall
# but sometimes goes straight towards players paddle,
#   in somewhat of a straight line,
#   or the center of players area,
#   maybe if they're losing??

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        random.seed()

        self.alive = None
        self.x = None
        self.y = None
        self.dx = 0
        self.dy = 0
        self.vx = 767.0 / (2050.0 / 16.5)  # 6.173535
        self.vy = None

        self.BOARD_TOP = 261
        self.BOARD_BOTTOM = -254
        self.BOARD_LEFT = -427
        self.BOARD_RIGHT = 421

        self.BALL_SIZE = 9

        self.penup()
        self.pensize(4)
        self.shape("square")
        self.color("white")
        self.birth()

    def draw(self):
        if self.alive:
            self.goto(self.x, self.y)
            self.begin_fill()
            for n in range(4):
                self.forward(self.BALL_SIZE)
                self.right(90)
            self.end_fill()

    def redraw(self):
        self.clear()
        self.draw()

    def die(self):
        self.alive = False
        self.clear()

    def birth(self):
        offset = random.choice([-12, 12])
        self.vy = random.uniform(-1.0, 1.0) * 1.4 * self.vx
        if self.vy > 0:
            self.dy = 1
        else:
            self.dy = -1
            self.vy = -1 * self.vy
        if offset > 0:
            self.dx = -1
        else:
            self.dx = 1
        self.x = -self.BALL_SIZE - 3 + offset

        # self.BOARD_TOP - 12
        # self.BOARD_BOTTOM + 21
        self.y = random.randint(self.BOARD_BOTTOM + 21, self.BOARD_TOP - 12)
        self.alive = True

    def move(self):
        self.x += (self.vx * self.dx)
        self.y += (self.vy * self.dy)

# vx:
# 2 seconds paddle to paddle no matter what
# d between 2 paddles = -427 + 35 - 421 - 46
# -392 - 375 == abs 767
# 767 / (2050/16.5)
#   = ~6.1734 px per tick

# boundries:
# self.x = self.BOARD_LEFT
# self.x = self.BOARD_RIGHT - 9
# self.y = self.BOARD_TOP
# self.y = self.BOARD_BOTTOM + 9
