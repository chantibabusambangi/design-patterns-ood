class Employee:
    def __init__(self, name, hours_worked, rate):
        self.name = name
        self.hours_worked = hours_worked
        self.rate = rate
class SalaryCalculator:
    def calculate(self, employee):
        return employee.hours_worked * employee.rate
class EmployeeRepository:
    def save(self, employee):
        print("Saving employee to database")
emp = Employee("Alice", 40, 50)

salary_calc = SalaryCalculator()
repo = EmployeeRepository()

salary = salary_calc.calculate(emp)
repo.save(emp)
#acheived with decoupling.