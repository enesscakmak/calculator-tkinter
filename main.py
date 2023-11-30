def main():
    root = Tk()
    calculator_logic = CalculatorLogic()
    app = Calculator(root, calculator_logic)
    root.mainloop()


if __name__ == "__main__":
    main()