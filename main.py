import tkinter as tk
from view import View


def main():
    root = tk.Tk()
    view = View(master=root)
    view.mainloop()

if __name__ == "__main__":
    main()