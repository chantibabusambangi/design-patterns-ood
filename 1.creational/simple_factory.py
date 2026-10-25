from abc import ABC, abstractmethod
# Product Interface
class Vehicle(ABC):
    @abstractmethod
    def get_details(self):
        pass
# Concrete Products
class Car(Vehicle):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def get_details(self):
        return f"Car → Brand: {self.brand}, Color: {self.color}"
class Bike(Vehicle):
    def __init__(self, brand, mileage, budget):
        self.brand = brand
        self.mileage = mileage
        self.budget = budget
    def get_details(self):
        return f"Bike → Brand: {self.brand}, Mileage: {self.mileage}, Budget: {self.budget}"
class Truck(Vehicle):
    def __init__(self, length, budget, color="White"):
        self.length = length
        self.budget = budget
        self.color = color
    def get_details(self):
        return f"Truck → Length: {self.length}, Budget: {self.budget}, Color: {self.color}"
#simple factory method(violates open-closed principle)
#this is wrong we should not use conditionals.but still practical.
class VehicleFactory_1:
    @staticmethod
    def create_vehicle(vehicle_type: str, **kwargs) -> Vehicle:
        if vehicle_type == "car":
            return Car(brand=kwargs["brand"],color=kwargs["color"])
        elif vehicle_type == "bike":
            return Bike(brand=kwargs["brand"],mileage=kwargs["mileage"],budget=kwargs["budget"])
        elif vehicle_type == "truck":
            return Truck(length=kwargs["length"],budget=kwargs["budget"],color=kwargs.get("color", "White"))
        else:
            raise ValueError("Invalid vehicle type")
#client code
def main():
    car = VehicleFactory.create_vehicle("car", brand="Toyota", color="Red")
    bike = VehicleFactory.create_vehicle("bike", brand="Yamaha", mileage=45, budget=150000)
    truck = VehicleFactory.create_vehicle("truck", length=30, budget=1200000)
    print(car.get_details())
    print(bike.get_details())
    print(truck.get_details())
if __name__ == "__main__":
    main()
'''
The Factory Method defines a method, which should be used for creating objects(without specifying their concrete classes) instead of using a direct constructor call. 
Subclasses can override this method to change the class of objects that will be created.
this follws open-closed prinicple,uses abstraction, flexibiility in creating objects.
'''