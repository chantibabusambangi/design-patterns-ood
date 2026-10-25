class Employee:
    def __init__(self, name, hours_worked, rate):
        self.name = name
        self.hours_worked = hours_worked
        self.rate = rate

    def calculate_salary(self):
        return self.hours_worked * self.rate

    def save_to_database(self):
        print("Saving employee to database")
#why this bad, this class is getting changed for every change in calculate_salary,save_to_database
#so we want our class to change for single reason.