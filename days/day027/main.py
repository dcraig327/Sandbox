from tkinter import *

window = Tk()
window.title("Hello tkinter")
window.minsize(width=500, height=300)

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    #    my_label.config(text="I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()
