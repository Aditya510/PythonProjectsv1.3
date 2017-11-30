import tkinter
def run():
    window = tkinter.Tk()
    window.title("Calculator")
    window.geometry("400x125")
    window.wm_iconbitmap('calculator.ico')
    window.configure(background="RoyalBlue1")
    def callback():
        a = int(xsquare.get())
        b = int(xcof.get())
        c = int(constant.get())
        d = (b**2) - (4*a*c)
        num1 = -b-d
        num2 = -b+d
        den = 2*a
        root1 = num1/den
        root2 = num2/den
        banner.configure(text = ("Your roots are:",root1,root2))
    banner = tkinter.Label(window, text="Welcome to my quadratic equation solver", bg="RoyalBlue1", fg='white')
    xsquare = tkinter.Entry(window)
    xcof = tkinter.Entry(window)
    constant = tkinter.Entry(window)
    button = tkinter.Button(window, text = "Submit", bg='floral white', command = callback)
    label1 = tkinter.Label(window, text="Co-efficient of x^2", bg='red', fg='white')
    label2 = tkinter.Label(window, text="   Co-efficient of x  ", bg='red', fg='white')
    label3 = tkinter.Label(window, text="        Constant         ", bg='red', fg='white')
    banner.grid(row=1)
    label1.grid(row=2)
    label2.grid(row=3)
    label3.grid(row=4)
    xsquare.grid(row=2,column=1)
    constant.grid(row=4,column=1)
    xcof.grid(row=3,column=1)
    button.grid(row=5)
    window.mainloop()

run()
