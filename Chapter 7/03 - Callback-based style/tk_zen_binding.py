import this
from tkinter import *
from tkinter import messagebox

rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
)


def main_window(root: Tk):
    frame = Frame(root)
    frame.pack()

    zen_button = Button(frame, text="Python Zen")
    zen_button.bind("<ButtonRelease-1>", show_zen)
    zen_button.pack(side=LEFT)


def show_zen(event):
    messagebox.showinfo("Zen of Python", this.s.translate(rot13))


if __name__ == "__main__":
    root = Tk()
    main_window(root)
    root.mainloop()
