import this
from tkinter import Tk, Frame, Button, LEFT, messagebox

rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
)


def main_window(root: Tk):
    frame = Frame(root)
    frame.pack()

    zen_button = Button(frame, text="Python Zen", command=show_zen)
    zen_button.pack(side=LEFT)


def show_zen():
    messagebox.showinfo("Zen of Python", this.s.translate(rot13))


if __name__ == "__main__":
    root = Tk()
    main_window(root)
    root.mainloop()
