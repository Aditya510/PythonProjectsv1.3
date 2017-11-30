from tkinter import * # Tkinter -> tkinter in Python 3

root = Tk()

def hello():
    print ("hello!")

# create a popup menu
menu = Menu(root, tearoff=0)
menu.add_command(label="Undo", command=hello)
menu.add_command(label="Redo", command=hello)

# create a frame
frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menu.post(event.x_root, event.y_root)

# attach popup to frame
frame.bind("<Button-3>", popup)

root.mainloop()
