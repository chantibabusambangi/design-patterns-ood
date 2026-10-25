from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass
class Add(Operation):
    def execute(self, a, b):
        return a + b
class Subtract(Operation):
    def execute(self, a, b):
        return a - b
class Multiply(Operation):
    def execute(self, a, b):
        return a * b
class Calculator:
    def calculate(self,operation:Operation, a, b):
        return operation.execute(a, b)
#usage
calc = Calculator()
print(calc.calculate(Add(), 10, 5))       # 15
print(calc.calculate(Subtract(), 10, 5))  # 5
print(calc.calculate(Multiply(), 10, 5))  # 50
#open for extensibility
class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
#acheived open for extensibility and closed for modification.
