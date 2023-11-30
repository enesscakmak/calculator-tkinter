from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self, master, calculator_logic):
        self.master = master
        master.title("Calculator")
        master.config(padx=4, pady=2)
        master.minsize(width=300, height=350)
        master.resizable(False, False)

        self.calculator_logic = calculator_logic

        frame = ttk.Frame(self.master, width=300, height=50, style="TFrame")
        frame.grid(row=0, column=0, columnspan=4, padx=0, pady=0)

        self.result_entry = Entry(frame, width=20, font="Arial 12", textvariable=StringVar(), justify="right",
                                  state="readonly", background="white", borderwidth=0, highlightthickness=0)
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=0, pady=0)

        self.entry = Entry(frame, width=20, font="Arial 20 bold", textvariable=StringVar(), justify="right",
                           state="readonly", background="white", borderwidth=0, highlightthickness=0)
        self.entry.grid(row=1, column=0, columnspan=4, padx=0, pady=0)

        buttons = [
            ("%", 2, 0), ("CE", 2, 1), ("C", 2, 2), ("⌫", 2, 3),
            ("1/x", 3, 0), ("x²", 3, 1), ("√x", 3, 2), ("/", 3, 3),
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("-", 5, 3),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3),
            ("+/-", 7, 0), ("0", 7, 1), (".", 7, 2), ("=", 7, 3)
        ]

        for button_text, row, col in buttons:
            ttk.Button(self.master, text=button_text, width=6, padding=15,
                       command=lambda b=button_text: self.on_button_click(b)).grid(row=row, column=col, padx=0, pady=0)

    def on_button_click(self, button_text):
        self.calculator_logic.button_click(button_text)
        self.update_entry()

    def update_entry(self):
        equation = self.calculator_logic.get_equation()
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, equation)

        self.entry.config(state="normal")
        self.entry.delete(0, END)
        self.entry.insert(0, equation)
        self.entry.config(state="readonly")


