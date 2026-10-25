class Calculator:
    def calculate(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        else:
            raise ValueError("Unsupported operation")
#usage
calc=Calculator()
print(calc.calculate(2,5,"+"))
print(calc.calculate(12,5,"-"))
print(calc.calculate(2,5,"*"))
