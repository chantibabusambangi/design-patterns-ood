from abc import ABC, abstractmethod
from enum import Enum
from collections import deque
import time
import uuid
class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
class Vehicle(ABC):
    def __init__(self, license_plate: str):
        self._license_plate = license_plate

    def get_license_plate(self):
        return self._license_plate

    @abstractmethod
    def get_size(self) -> VehicleSize:
        pass
class Motorcycle(Vehicle):
    def get_size(self):
        return VehicleSize.SMALL
class Car(Vehicle):
    def get_size(self):
        return VehicleSize.MEDIUM
class Truck(Vehicle):
    def get_size(self):
        return VehicleSize.LARGE
class ParkingSpot(ABC):
    def __init__(self, spot_id: int):
        self.spot_id = spot_id
        self.vehicle = None

    def is_free(self):
        return self.vehicle is None

    def park(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def unpark(self):
        self.vehicle = None

    @abstractmethod
    def get_size(self) -> VehicleSize:
        pass
class CompactSpot(ParkingSpot):
    def get_size(self):
        return VehicleSize.SMALL
class RegularSpot(ParkingSpot):
    def get_size(self):
        return VehicleSize.MEDIUM
class OversizedSpot(ParkingSpot):
    def get_size(self):
        return VehicleSize.LARGE
class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle_plate = vehicle.get_license_plate()
        self.spot_id = spot.spot_id
        self.entry_time = time.time()
class ParkingManager:
    def __init__(self):
        self.free_spots = {
            VehicleSize.SMALL: deque(),
            VehicleSize.MEDIUM: deque(),
            VehicleSize.LARGE: deque()
        }
        self.occupied_spots = {}  # spot_id -> ParkingSpot

    def add_spot(self, spot: ParkingSpot):
        self.free_spots[spot.get_size()].append(spot)

    def assign_spot(self, vehicle: Vehicle) -> ParkingSpot:
        size = vehicle.get_size()
        if not self.free_spots[size]:
            raise Exception("No spot available")

        spot = self.free_spots[size].popleft()
        spot.park(vehicle)
        self.occupied_spots[spot.spot_id] = spot
        return spot

    def release_spot(self, spot_id: int):
        spot = self.occupied_spots.pop(spot_id)
        spot.unpark()
        self.free_spots[spot.get_size()].append(spot)
class ParkingLot:
    def __init__(self):
        self.manager = ParkingManager()

    def add_parking_spot(self, spot: ParkingSpot):
        self.manager.add_spot(spot)

    def enter(self, vehicle: Vehicle) -> Ticket:
        spot = self.manager.assign_spot(vehicle)
        return Ticket(vehicle, spot)

    def exit(self, ticket: Ticket):
        self.manager.release_spot(ticket.spot_id)
parking_lot = ParkingLot()

# Add spots
parking_lot.add_parking_spot(CompactSpot(1))
parking_lot.add_parking_spot(RegularSpot(2))
parking_lot.add_parking_spot(OversizedSpot(3))

# Vehicles
bike = Motorcycle("BIKE-101")
car = Car("CAR-202")

# Park
ticket1 = parking_lot.enter(bike)
ticket2 = parking_lot.enter(car)

print("Bike parked at spot:", ticket1.spot_id)
print("Car parked at spot:", ticket2.spot_id)

# Unpark
parking_lot.exit(ticket1)
print("Bike exited")
