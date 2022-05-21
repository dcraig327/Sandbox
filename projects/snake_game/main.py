# from turtle import Screen
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# classes
# snake, food, scoreboard
# game_running = True

# adding food.py and random on eat and growing snake
# turtle is 25W, 19H
# turtle from center is -10W, ?+25W
# turtle from center is

# ?L, 0, 12r
WIDTH = 600
HEIGHT = 600


class Game:

    def __init__(self):
        self.tick_ms_delay = 100

        self.screen = turtle.Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.delay(0)
        self.screen.bgcolor("black")
        self.screen.title("snake_game")

        self.snake = Snake(self.screen)
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.game_active = True

        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(exit, "Escape")

        self.tick()
        self.screen.listen()
        self.screen.mainloop()

    def end_game(self):
        # self.game_active = False
        # self.scoreboard.game_over()
        self.scoreboard.reset()
        self.snake.reset()

    def tick(self):
        if self.game_active:
            turtle.ontimer(self.tick, self.tick_ms_delay)
            self.snake.move()
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.grow()
                self.scoreboard.increase()
                self.tick_ms_delay = int(0.95 * self.tick_ms_delay)
            x = self.snake.head.xcor()
            y = self.snake.head.ycor()
            if x > 280 or x < -280 or y > 280 or y < -280:
                self.end_game()
            for segment in self.snake.segments[1:]:
                # if self.snake.head == segment:
                #     continue
                if self.snake.head.distance(segment) < 10:
                    self.end_game()


game = Game()
