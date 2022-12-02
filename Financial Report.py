from tkinter import *

root = Tk()
root.title("Income Report")
WIDTH, HEIGHT = 500,650
root.geometry('{}x{}'.format(WIDTH, HEIGHT))

frame = Frame(root, bg="#9FE2BF", relief=SUNKEN)
frame.place(x=0, y=-20, width=540, height=360)

def myClick():
    myLbl1 = Label(root, text="Enter your name", font="Cooper 13 bold")
    myLbl1.grid(padx=30, pady=30)
    txt = Entry(root, width=30)
    txt.place(x=150, y=390)
    myLbl2 = Label(root, text="Enter your Transaction No.", font="Cooper 13 bold")
    myLbl2.grid(padx=30, pady=30)
    txt = Entry(root, width=30)
    txt.place(x=150, y=485)
        

myButton1 = Button(root, text="Reciept", padx=20, pady=20, command=myClick, fg="#CCCCFF", bg="#6495ED", width=40, height=3, font="Cooper 13 bold")
myButton1.grid(padx=30, pady=30)


def myClick2():
    myLbl3 = Label(root, text="Your income from this transaction is", font="Cooper 13 bold")
    myLbl3.grid(padx=30, pady=30)


myButton2 = Button(root, text="Revenue", padx=20, pady=20, command=myClick2, fg="#CCCCFF", bg="#6495ED", width=40, height=3, font="Cooper 13 bold")
myButton2.grid(padx=30, pady=30)

root.mainloop()
