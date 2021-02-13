import math
from tkinter import *


def tempo_to_speed(mins, secs):
    total_seconds = 60 * mins + secs
    v = 3600 / total_seconds
    print(v, "km / h")


def speed_to_tempo(v):
    total_seconds = 3600 / v
    secs = total_seconds % 60
    mins = math.floor(total_seconds / 60)
    return mins, secs



root = Tk()
root.title("Test title")
root.geometry("250x200")


def calc():
    mins, secs = speed_to_tempo(float(minuteInput.get()))
    out = Label(root, text=str(mins) + ":" + str(int(secs)) + " min / km")
    out.grid(row=3, column=0)


myLabel = Label(root, text="Enter the speed")
myLabel.grid(row=0, column=0)

minuteInput = Entry(root, width=30)
minuteInput.grid(row=1, column=0)

minuteButton = Button(root, text="Convert", command=calc)
minuteButton.grid(row=1, column=1)

root.mainloop()