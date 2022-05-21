import pandas as pd

################################################################################
# load weather_data.csv
# into a list
# each line is its own item

# filename = "weather_data.csv"
# with open(filename) as file:
#     lines = []
#     data = file.readlines()
#     # for line in file:
#     #     lines.append(line.strip())

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         #this fails on negative numbers
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)


# data = pd.read_csv("weather_data.csv")


# def c_to_f(temp):
#     return temp * 9 / 5 + 32
#
#
# def f_to_c(temp):
#     return (temp - 32) * 5 / 9


# d = data.to_dict()
# print(d)
#
# temps = data["temp"].to_list()
# print(temps)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# get monday temp. convert to degF


# monday = data[data.day == "Monday"]
# c = float(monday.temp)
# print(c)
# f = c_to_f(c)
# print(f)
# print(f_to_c(f))

# Create DF from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
################################################################################

# create a csv
# to count the total of all squirrels by color
# "squirrel_count.csv"

squirrels = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# squirrels_color = squirrels["Primary Fur Color"]
# unique_squirrels_color = squirrels_color.value_counts()
# unique_squirrels_color.to_csv("squirrel_count.csv")


grey_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
