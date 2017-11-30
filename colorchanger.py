import tkinter
window = tkinter.Tk()
window.title("Color changer")
def makered():
    window.configure(background="RoyalBlue1")
def makegreen():
    window.configure(background="green")
button = tkinter.Button(window, text = "Blue", command = makered)
button2 = tkinter.Button(window, text = "Green", command = makegreen)
button.pack()
button2.pack()
window.mainloop()
