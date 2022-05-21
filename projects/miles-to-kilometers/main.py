from tkinter import *


class MilesToKilometers:
    def __init__(self):
        self.window = Tk()
        self.window.title("Miles To Kilometers Converter")
        #self.window.minsize(width=500, height=300)
        self.label1 = Label(text="Miles")
        self.label1.grid(column=2, row=0)
        self.label2 = Label(text="is equal to")
        self.label2.grid(column=0, row=1)
        self.label3 = Label(text="32")
        self.label3.grid(column=1, row=1)
        self.label4 = Label(text="Km")
        self.label4.grid(column=2, row=1)

        self.input = Entry()
        self.input.grid(column=1, row=0)

        self.button = Button(text="Calculate", command=self.button_press)
        self.button.grid(column=1, row=2)


        self.window.mainloop()

    def button_press(self):
        km = float(self.input.get()) * 1.609
        self.label3.config(text=f"{km}")


#4 labels
#input
#button

MilesToKilometers()
