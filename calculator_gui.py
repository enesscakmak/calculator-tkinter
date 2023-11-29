from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.config(padx=4, pady=2)
        master.minsize(width=300, height=350)
        master.resizable(False, False)

        self.create_gui()

    def create_gui(self):
        frame = ttk.Frame(self.master, width=300, height=50, style="TFrame")
        frame.grid(row=0, column=0, columnspan=4, padx=0, pady=0)

        entry = Entry(frame, width=20, font="Arial 20 bold", justify="right", state="readonly",
                      background="white", borderwidth=0)

        entry.grid(row=0, column=0, columnspan=4, padx=0, pady=0)

        ttk.Button(self.master, text="%", width=6, padding=15).grid(row=1, column=0, padx=0, pady=0)
        ttk.Button(self.master, text="CE", width=6, padding=15).grid(row=1, column=1, padx=0, pady=0)
        ttk.Button(self.master, text="C", width=6, padding=15).grid(row=1, column=2, padx=0, pady=0)
        ttk.Button(self.master, text="⌫", width=6, padding=15).grid(row=1, column=3, padx=0, pady=0)
        ttk.Button(self.master, text="1/x", width=6, padding=15).grid(row=2, column=0, padx=0, pady=0)
        ttk.Button(self.master, text="x²", width=6, padding=15).grid(row=2, column=1, padx=0, pady=0)
        ttk.Button(self.master, text="√x", width=6, padding=15).grid(row=2, column=2, padx=0, pady=0)
        ttk.Button(self.master, text="÷", width=6, padding=15).grid(row=2, column=3, padx=0, pady=0)
        ttk.Button(self.master, text="7", width=6, padding=15).grid(row=3, column=0, padx=0, pady=0)
        ttk.Button(self.master, text="8", width=6, padding=15).grid(row=3, column=1, padx=0, pady=0)
        ttk.Button(self.master, text="9", width=6, padding=15).grid(row=3, column=2, padx=0, pady=0)
        ttk.Button(self.master, text="x", width=6, padding=15).grid(row=3, column=3, padx=0, pady=0)
        ttk.Button(self.master, text="4", width=6, padding=15).grid(row=4, column=0, padx=0, pady=0)
        ttk.Button(self.master, text="5", width=6, padding=15).grid(row=4, column=1, padx=0, pady=0)
        ttk.Button(self.master, text="6", width=6, padding=15).grid(row=4, column=2, padx=0, pady=0)
        ttk.Button(self.master, text="-", width=6, padding=15).grid(row=4, column=3, padx=0, pady=0)
        ttk.Button(self.master, text="1", width=6, padding=15).grid(row=5, column=0, padx=0, pady=0)
        ttk.Button(self.master, text="2", width=6, padding=15).grid(row=5, column=1, padx=0, pady=0)
        ttk.Button(self.master, text="3", width=6, padding=15).grid(row=5, column=2, padx=0, pady=0)
        ttk.Button(self.master, text="+", width=6, padding=15).grid(row=5, column=3, padx=0, pady=0)
        ttk.Button(self.master, text="+/-", width=6, padding=15).grid(row=6, column=0, padx=0, pady=0)
        ttk.Button(self.master, text="0", width=6, padding=15).grid(row=6, column=1, padx=0, pady=0)
        ttk.Button(self.master, text=".", width=6, padding=15).grid(row=6, column=2, padx=0, pady=0)
        ttk.Button(self.master, text="=", width=6, padding=15).grid(row=6, column=3, padx=0, pady=0)


def main():
    root = Tk()
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
