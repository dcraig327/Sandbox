import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.FINISH_LINE_Y = 280

        self.player = Player()
        self.scoreboard = Scoreboard()
        self.car_manager = CarManager()
        self.game_is_on = True

        self.screen.listen()
        self.screen.onkeypress(self.game_over, 'Escape')
        self.screen.onkeypress(self.player.move, 'Up')

        self.loop()

    def loop(self):
        while self.game_is_on:
            time.sleep(0.1)
            self.update()
            self.draw()
        self.scoreboard.game_over()
        self.screen.exitonclick()

    def update(self):
        self.car_manager.move()
        if self.player.ycor() >= self.FINISH_LINE_Y:
            self.player.start()
            self.scoreboard.increase()
            self.car_manager.increase()
        for car in self.car_manager.cars:
            if self.player.distance(car.xcor()-20, car.ycor()) < 15:
                self.game_over()

    def draw(self):
        self.screen.update()

    def game_over(self):
        self.game_is_on = False

game = Game()

# cars randomly generated along y-axis move right->left
# turtle hits top edge, it moves back and levels up, cars increase, scoreboard increase
# collide with car is gg and everything stops
# "GAME OVER"
