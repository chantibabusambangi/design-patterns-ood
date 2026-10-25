class House:
    def __init__(self):
        self.garage = False
        self.pool = False
        self.garden = False
        self.statues = False

    def get_details(self):
        print (f"House(garage={self.garage}, "
                f"pool={self.pool}, "
                f"garden={self.garden}, "
                f"statues={self.statues})")
#builder: complex object created step by step.

class HouseBuilder:
    def __init__(self):
        self.house = House()
    def add_garage(self):
        self.house.garage = True
        return self
    def add_pool(self):
        self.house.pool = True
        return self
    def add_garden(self):
        self.house.garden = True
        return self

    def add_statues(self):
        self.house.statues = True
        return self
    def build(self):
        return self.house
builder=HouseBuilder()
builder.add_garage()
builder.add_garden()
myhouse=builder.build()
myhouse.get_details()
#director is optional
