from tkinter import *
import random

root = Tk()

root.title("ASCII")
root.geometry("400x400")
root.configure(background = "Snow")

LabelList = Label(root)
LabelChoose = Label(root)
List = ["Mat", "Basket", "Snacks", "Lunch", "Other Cool Stuff"]
LabelList["text"] = "Listed items: " + str(List)

def Noice():
    randomlist = random.sample(range(0, 5), 1)
    LabelChoose["text"] = "Choose Item No." + str(randomlist) + " now!"

Button = Button(root, text = "What should I choose?", command = Noice)

LabelList.place(relx=0.5, rely=0.5, anchor=CENTER)
Button.place(relx=0.5, rely=0.6, anchor=CENTER)
LabelChoose.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()


