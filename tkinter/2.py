import tkinter as tk

w = tk.Tk()
for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master= w,
            relief= tk.GROOVE,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text = f"Row{i}\nColumn{j}")
        label.pack()
        

w.mainloop()
