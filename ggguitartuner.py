import tkinter

window = tkinter.Tk()

MyTitle = tkinter.Label(window, text="GG Guitar Tuner",font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="OK")
MyButton.pack()

window.mainloop()