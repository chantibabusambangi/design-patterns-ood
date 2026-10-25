from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    #def role(self): return "developer"
    def work(self):
        print("Writing code")
class Tester(Employee):
    def work(self):
        print("Testing application")
    #def role(self): return "tester"
class Designer(Employee):
    def work(self):
        print("Designing UI")
    #def role(self): return "designer"
class Manager:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee: Employee):
        self.employees.append(employee)
    def manage(self):
        for emp in self.employees:
            emp.work()

#High-level modules should not depend on low-level modules.
#Both should depend on abstractions.
#Abstractions should not depend on details. Details should depend on abstractions.

#manager dont need to know the employee what type he was.
#if manager wants to know, we can add role method in each of employeetype classes.
#like in developer class, we can add role method.