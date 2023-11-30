import math
from ast import parse
from re import sub


class CalculatorLogic:
    def __init__(self):
        self.equation = ""
        self.result = ""

    def button_click(self, button_text):
        if button_text == "=":
            self.calculate_result()
        elif button_text == "⌫":
            self.equation = self.equation[:-1]
        elif button_text == "C":
            self.clear_all()
        elif button_text == "CE":
            self.clear_entry()
        elif button_text == "+/-":
            self.negate()
        elif button_text == "1/x":
            self.perform_unary_operation("1/(", ")")
        elif button_text == "√x":
            self.perform_square_root()
        elif button_text == "x²":
            self.perform_unary_operation("(", ")**2")
        else:
            self.equation += str(button_text)

    import ast
    import re

    def calculate_result(self):
        try:
            # Remove leading zeros from numbers
            sanitized_equation = sub(r'\b0+(\d+)', r'\1', self.equation)

            parsed_equation = parse(sanitized_equation, mode='eval')
            compiled_code = compile(parsed_equation, '<string>', 'eval')
            result = eval(compiled_code)

            if isinstance(result, (float, int)):
                if math.isinf(result):
                    raise ZeroDivisionError
                self.clear_entry()
                self.result = str(result)
                self.equation = str(result)
            else:
                raise ValueError("Invalid result type")
        except ZeroDivisionError:
            self.result = "Cannot divide by zero"
        except Exception as e:
            self.result = "Error"

    def clear_all(self):
        self.result = ""
        self.clear_entry()

    def clear_entry(self):
        if self.result:
            self.equation = self.result
        else:
            self.equation = ""

    def negate(self):
        try:
            self.equation = str(eval("-" + self.equation))
        except Exception as e:
            self.equation = "Error"

    def perform_unary_operation(self, prefix, suffix):
        last_operand = self.get_last_operand()
        try:
            if last_operand:
                operation_result = str(eval(prefix + last_operand + suffix))
                self.equation = self.equation.rsplit(last_operand, 1)[0] + operation_result
            else:
                self.equation = "Error"
        except Exception as e:
            self.equation = "Error"

    def perform_square_root(self):
        last_operand = self.get_last_operand()
        try:
            if last_operand:
                value = eval(last_operand)
                if value >= 0:
                    root_result = str(math.sqrt(value))
                    self.equation = self.equation.rsplit(last_operand, 1)[0] + root_result
                else:
                    self.equation = "Error"
            else:
                self.equation = "Error"
        except Exception as e:
            self.equation = "Error"

    def get_last_operand(self):
        symbols = set("+-*/")
        reversed_equation = self.equation[::-1]
        last_operand = ""
        for char in reversed_equation:
            if char in symbols:
                break
            last_operand += char
        return last_operand[::-1]

    def get_equation(self):
        return self.equation if self.equation else self.result

