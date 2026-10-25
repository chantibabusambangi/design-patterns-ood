from abc import ABC,abstractmethod
from enum import Enum
import time
from collections import deque
class Get_vehicle_type(Enum):
    bike=1
    car=2
    truck=3
    bus=4

class Vehicle:
    def __init__(self,vehicle_license,vehicle_name):
        self.vehicle_license=vehicle_license
        self.vehicle_name=vehicle_name
        self.vehicle_type=Get_vehicle_type[vehicle_name].value
class Slot:
    def __init__(self,slot_id,slot_type):
        self.slot_id=slot_id
        self.slot_type=slot_type #1-4
class Parking_lot:
    def __init__(self,slots): #list of (list of slot objects) 4 lists.
        bike_slots=deque(slots[0]) #free slots(slot objects)
        car_slots=deque(slots[1])
        truck_slots=deque(slots[2])
        bus_slots=deque(slots[3])
        self.slots=[bike_slots,car_slots,truck_slots,bus_slots] #list of deque(slot objects).
        self.map={} #vehicle license:(slot object,start_time)
    def park(self,vehicle):
        vehicle_type=vehicle.vehicle_type
        free_slot=None
        for i in range(vehicle_type-1,4): #bike can park at (bike,car,truck,bus) slots.
            if(self.slots[i]):
                free_slot=self.slots[i].popleft()
                break
        if(not free_slot):
            print(f"No slot left{vehicle.vehicle_name,vehicle.license}")
            return 
        self.map[vehicle.vehicle_license]=(free_slot,time.time())
        print(f"successfully parked the vehicle, ticket: {vehicle.vehicle_license} at {free_slot.slot_type},time.time()")
        return free_slot
    def unpark(self,vehicle):
        slot,start_time=self.map[vehicle.vehicle_license] #free slot
        del self.map[vehicle.vehicle_license]
        self.slots[slot.slot_type-1].append(slot)
        print(f"successfully unparked the vehicle:{vehicle.vehicle_name}")
        price=self.get_price(vehicle,slot,start_time)
        print(f"price={price}")
    def get_price(self,vehicle,slot,start_time):
        end_time=time.time()
        price=(end_time-start_time)*vehicle.vehicle_type
        return price
    def add_free_slot(self,slot):
        self.slots[slot.slot_type-1].append(slot)
        print(f"successfully added the slot:{slot.slot_type}")
    def free_slot_details(self):
        vals=[]
        for i in range(4):
            vals.append(len(self.slots[i]))
        print(f"free slot details=> bikes:{vals[0]},cars:{vals[1]},trucks:{vals[2]},buses:{vals[3]}")

#client code
slots=[[] for _ in range(4)]
for i in range(1,5):
    for j in range(5):
        slots[i-1].append(Slot(j,i)) #slot id,slot type
print(len(slots),len(slots[0]))
my_lot=Parking_lot(slots)

vehicles=[[Vehicle("license_bike"+str(i),"bike") for i in range(1,7)]]
vehicles.append([Vehicle("license_car"+str(i),"car") for i in range(1,4)])
vehicles.append([Vehicle("license_truck"+str(i),"truck") for i in range(1,4)])
vehicles.append([Vehicle("license_bus"+str(i),"bus") for i in range(1,3)])
my_lot.free_slot_details()
for vehicle_list in vehicles:
    for vehicle in vehicle_list:
        my_lot.park(vehicle)
my_lot.free_slot_details()
my_lot.unpark(vehicles[0][0])
print("successfully completed!")