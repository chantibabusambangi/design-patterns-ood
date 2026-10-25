'''ffor creating different vehicles it may have different parameters right!
for car it has parametrs like color,brand, 
for truck it has parameters like length(length of truck),budget,color(optinal paramter) lly 
for bike you may have parametres like brand,milage,budget. 
so we can use factory method for this kind of problem right
'''
from abc import ABC, abstractmethod
#abstract class Vehicle
class Vehicle(ABC):
    @abstractmethod
    def get_details(self):
        pass
#concrete products #subclasses
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
        return f"Bike → Brand: {self.brand}, Mileage: {self.mileage} km/lit, Budget: {self.budget}"
class Truck(Vehicle):
    def __init__(self, length, budget, color="White"):  # color optional parameter
        self.length = length
        self.budget = budget
        self.color = color
    def get_details(self):
        return f"Truck → Length: {self.length} ft,Budget: {self.budget}, Color: {self.color}"
#GOF factory method
#Creation logic must be decided by subclasses, not by conditionals
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass
#concrete factories(subclasses decide creation)
class CarFactory(VehicleFactory):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def create_vehicle(self) -> Vehicle:
        #inside this, there can be a complex steps of creation
        return Car(self.brand, self.color)
class BikeFactory(VehicleFactory):
    def __init__(self, brand, mileage, budget):
        self.brand = brand
        self.mileage = mileage
        self.budget = budget
    def create_vehicle(self) -> Vehicle:
        #inside this, there can be a complex steps of creation
        return Bike(self.brand, self.mileage, self.budget)
class TruckFactory(VehicleFactory):
    def __init__(self, length, budget, color="White"):
        self.length = length
        self.budget = budget
        self.color = color
    #we can add some other features here if object has a compelex design
    def create_vehicle(self) -> Vehicle:
        #inside this, there can be a complex steps of creation
        return Truck(self.length, self.budget, self.color)
'''
this factory method feels like holding the details,
but this is exactly used in complex creation of objects.
TruckFactory can create many truck of same models.
'''

#client code
#Client depends only on Vehicle abstraction,which Supports different constructor parameters
def main():
    car_factory=CarFactory("Toyota", "Red")
    Bike_factory=BikeFactory("Yamaha", 45, 150000)
    Truck_Factory=TruckFactory(30, 1200000)
    
    c1=car_factory.create_vehicle()
    c2=car_factory.create_vehicle()
    print(c1.get_details())
    print(c2.get_details())

    b1=Bike_factory.create_vehicle()

    t1=Truck_Factory.create_vehicle()

if __name__ == "__main__":
    main()
'''
The Factory Method defines a method, which should be used for creating objects(without specifying their concrete classes) instead of using a direct constructor call. 
Subclasses can override this method to change the class of objects that will be created.
this follws open-closed prinicple,uses abstraction, flexibiility in creating objects.
'''