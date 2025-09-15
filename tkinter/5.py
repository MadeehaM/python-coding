from tkinter import *

root = Tk()
root.title("Main")
root.geometry('400x300')

def topwin():
    top = Toplevel()
    top.geometry('180x180')
    top.title("Top Level")
    l = Label(top, text="This is the toplevel window")
    l.pack()
    top.mainloop()

l2 = Label(root, text = "This is main window")
B = Button(root, text="Click here to open another window", command=topwin)
l2.pack()
B.pack()
root.mainloop()