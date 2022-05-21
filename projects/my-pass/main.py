from random import choice, randint, shuffle
from tkinter import *
import pyperclip
import json


# ---------------------------- ------------------------------- #

# E = L * log2(R),
# R = pool size (number of possible characters)
# L = password length
# E = Entropy in bits uses 1 decimal precision

# It doesn't matter how many bits of entropy a password contains if it's on a dictionary of common passwords,
# as these are usually tried first.

# For generating a master password, a good starting point is to pick three random words from a dictionary. With a
# dictionary of 350,000 words, our character set effectively becomes 350,000. I'll take "checkered", "waving",
# and "spider". These three are easy to remember, and just appending them into "checkeredwavingspider" which already
# gives 56 bits of entropy (length of 3 in a character set of 350,000). To increase this further, I’ll change the
# second character of each word, and add a symbol as a separator between words – “cHeckered!wAving;sPider”. This
# password now has a character set of almost random characters, is 23 characters in length, and won't be found on any
# attacker's word lists, giving a total of 150 bits of entropy. It's easier to remember than completely random
# characters and is almost impossible to guess.

# A password with n bits of entropy would require 2^n guesses to guarantee that password will be found. For some
# context, it's realistic that a normal person with a single graphics card on their computer can guess about 2^49
# passwords per day. Someone with a data mining system might be able to get 2^55 passwords or possibly more,
# depending on their hardware. (Note: these numbers are based on GPU hash breaking and require a data dump of
# password hashes. Web based brute forcing would be much slower.)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# we allow the user to enter passwords OR generate a password based on the user's criteria
# calculate entropy for the password entered
# user's criteria includes
#   desired entropy
#   allow lower/upper/numbers/symbols each separately
# as a white hat password cracker pentest, find the password entered in the keyword list AND permutations
#   kali word list, want to have this be dynamic and pull from the source repo

# https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt


# # ----------------------------  ------------------------------- #
# # 33 symbols
# # 10 numbers
# # 26 upper
# # 26 lower
# # 95 total
# class PasswordGenerator:
#     SYMBOLS = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
#                '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#     NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#              'v', 'w', 'x', 'y', 'z']
#     ROCKYOU = "rockyou.txt"
#
#     def lookup(self, password):
#         print(self.ROCKYOU)
#         with open(self.ROCKYOU, "r") as file:
#             print(file.readline())
#
#     def generate(self):
#         # nr_letters = random.randint(8, 10)
#         # nr_symbols = random.randint(2, 4)
#         # nr_numbers = random.randint(2, 4)
#         #
#         # password_list = []
#         #
#         # for char in range(nr_letters):
#         #     password_list.append(random.choice(letters))
#         #
#         # for char in range(nr_symbols):
#         #     password_list += random.choice(symbols)
#         #
#         # for char in range(nr_numbers):
#         #     password_list += random.choice(numbers)
#         #
#         # password = ""
#         # for char in password_list:
#         #     password += char
#
#         self.lookup("test")
#
#         password = ['1', '2', '3']
#         random.shuffle(password)
#         password_string = ''.join(str(e) for e in password)
#         print(password_string)
#         return password_string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
class PasswordFile:
    PASSWORD_FILENAME = "data.json"

    # scan if already in file and update it, if possible
    def add(self, url, login, password):
        new_data = {
            url: {
                "login": login,
                "password": password
            }
        }
        data = new_data

        try:
            # need to validate if the file is empty, invalid
            with open(self.PASSWORD_FILENAME, "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            pass
        finally:
            with open(self.PASSWORD_FILENAME, "w") as file:
                json.dump(data, file, indent=4)

    def find(self, url):
        data = {}
        try:
            with open(self.PASSWORD_FILENAME, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return None
        try:
            if data[url]:
                return data[url]
        except IndexError:
            pass

        return None


# ---------------------------- UI SETUP ------------------------------- #

class Window:
    # modal window
    TITLE = "Password Manager"
    FONT_LABEL = ("Arial", 14, "normal")
    FONT_BUTTON = ("Arial", 10, "normal")
    FONT_ENTRY = ("Arial", 14, "normal")

    def __init__(self):
        self.window = Tk()
        self.window.title(self.TITLE)
        self.window.config(padx=20, pady=20)
        self.password_file = PasswordFile()

        self.canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.my_pass_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.my_pass_image)
        self.canvas.grid(column=1, row=0)

        self.website_label = Label(text="Website:", font=self.FONT_LABEL)
        self.website_label.grid(column=0, row=1)

        self.email_username_label = Label(text="Email/Username:", font=self.FONT_LABEL)
        self.email_username_label.grid(column=0, row=2)

        self.password_label = Label(text="Password:", font=self.FONT_LABEL)
        self.password_label.grid(column=0, row=3)

        self.website = StringVar(name="website")
        self.website.trace("w", self.update_entries)
        self.website_entry = Entry(width=23, textvariable=self.website, font=self.FONT_ENTRY)
        self.website_entry.grid(column=1, row=1)
        self.website_entry.focus()

        self.search_button = Button(text="Search", width=15, font=self.FONT_BUTTON, state=DISABLED,
                                    command=self.search_command)
        self.search_button.grid(column=2, row=1)

        self.email_username = StringVar(name="email_username")
        self.email_username.trace("w", self.update_entries)
        self.email_username_entry = Entry(width=35, textvariable=self.email_username, font=self.FONT_ENTRY)
        self.email_username_entry.grid(column=1, row=2, columnspan=2)

        self.password = StringVar(name="password")
        self.password.trace("w", self.update_entries)
        self.password_entry = Entry(width=23, textvariable=self.password, font=self.FONT_ENTRY)
        self.password_entry.grid(column=1, row=3)

        self.generate_password_button = Button(text="Generate Password", width=15, font=self.FONT_BUTTON,
                                               command=self.generate_password_command)
        self.generate_password_button.grid(column=2, row=3)

        self.add_password_button = Button(text="Add", width=15, font=self.FONT_BUTTON,
                                          command=self.add_password_command,
                                          state=DISABLED)
        self.add_password_button.grid(column=2, row=4)

        self.email_username_entry.insert(END, "my@email.com")
        self.window.mainloop()

    def update_entries(self, *args):
        if self.website.get() and self.email_username.get() and self.password.get():
            self.add_password_button.config(state=NORMAL)
        else:
            self.add_password_button.config(state=DISABLED)

        if args[0] == "website":
            if self.website.get():
                self.search_button.config(state=NORMAL)
            else:
                self.search_button.config(state=DISABLED)

    def search_command(self):
        entry = self.password_file.find(self.website.get())
        self.email_username.set(entry["login"])
        self.password.set(entry["password"])

    def generate_password_command(self):
        password = generate_password()
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def add_password_command(self):
        self.password_file.add(self.website_entry.get(), self.email_username_entry.get(), self.password_entry.get())
        self.website_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.website_entry.focus()


window = Window()
