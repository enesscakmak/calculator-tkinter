from calculator_logic import CalculatorLogic
from calculator_gui import Calculator
from tkinter import Tk


def main():
    root = Tk()
    calculator_logic = CalculatorLogic()
    app = Calculator(root, calculator_logic)
    root.mainloop()


if __name__ == "__main__":
    main()
