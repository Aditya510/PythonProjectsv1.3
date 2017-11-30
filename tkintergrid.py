import tkinter
grid = tkinter.Tk()

def callback():
    print("click!")

b = tkinter.Button(grid, text="OK", command=callback)
b.pack()
grid.mainloop()
