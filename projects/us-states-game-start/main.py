import turtle
import pandas as pd


class Game:
    DEFAULT_WINDOW_TITLE = "US States Game"
    WINDOW_TITLE = "/50 States Correct"
    WINDOW_PROMPT = "What's another state name? (Leave blank to to exit)"
    IMAGE_FILENAME = "blank_states_img.gif"
    STATES_FILENAME = "50_states.csv"

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title(self.WINDOW_TITLE)
        self.screen.addshape(self.IMAGE_FILENAME)
        turtle.shape(self.IMAGE_FILENAME)
        # self.screen.delay(0)
        # self.screen.tracer(0, 0)
        self.states = pd.read_csv(self.STATES_FILENAME)
        self.score = 0

        print(self.states)

        while True:
            if self.score:
                title = str(self.score) + self.WINDOW_TITLE
            else:
                title = self.DEFAULT_WINDOW_TITLE
            user_data = self.screen.textinput(title=title, prompt=self.WINDOW_PROMPT)
            if user_data == "":
                exit()
            user_data = user_data.capitalize()
            x = 0
            y = 0
            selection = self.states[self.states.state == user_data]
            if len(selection):
                x = int(selection.x)
                y = int(selection.y)
                self.score += 1

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x, y)
            t.write(f"{user_data}")


Game()

#
# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#
# # after any correct guess, title="1/50 States Correct"
# # after any incorrect guess, title remains the same

# squirrels = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# # squirrels_color = squirrels["Primary Fur Color"]
# # unique_squirrels_color = squirrels_color.value_counts()
# # unique_squirrels_color.to_csv("squirrel_count.csv")
#
#
# grey_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
#
