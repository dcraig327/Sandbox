from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
lane_width = 30
turtles = []


# 20 from left
# 25 from center
# 50 from each other

def create_turtles():
    # 125 to -125 step 50
    for n in range(0, 6):
        t = Turtle(shape="turtle")
        t.fillcolor(colors[n])
        t.penup()
        t.goto(x=-240, y=lane_width * 2.5 - n * lane_width)
        turtles.append(t)


def start_race():
    winners = []
    race_active = True
    random.seed()
    while race_active:
        for n in range(0, 6):
            dist = random.randint(0, 10)
            turtles[n].forward(dist)
        for n in range(0, 6):
            if turtles[n].xcor() >= 225:
                winners.append(colors[n])
                race_active = False
    print(winners)
    user_won = False
    for n in winners:
        if user_bet == n:
            user_won = True
    if user_won:
        print("You Won!")
    else:
        print("You Lost.")


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? ")
create_turtles()
start_race()

# for n in range(0,6):
#    turtles[n].setx(227-n)


# t.goto(x=-240,y=-184)
# turtle sprite is flush TopRight at x=225,y=190
# t.goto(x=-240,y=-183 or -184)

# screen is -250 to 250

screen.exitonclick()
# 240 left
# 225 right
# ? top
# ? bot
# turtle is 25W, 19H
# turtle from center is -10W, ?+25W
# turtle from center is
