from abc import ABC, abstractmethod
#observer/subscribers interface
class Observer(ABC): 
    @abstractmethod
    def update(self, temperature):
        pass
#subject/publisher interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer): #add subscriber
        pass
    @abstractmethod
    def detach(self, observer): #remove-subscriber
        pass
    @abstractmethod
    def notify(self):
        pass

#concrete subject/publisher
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)
    def set_temperature(self, temperature):
        print(f"\nWeatherStation: New temperature = {temperature}")
        self._temperature = temperature
        self.notify()

#concrete observers/subscribers(need updates on weather)
#phonemedia, tv dispaly
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone Display updated: Temperature = {temperature}")
class TVDisplay(Observer):
    def update(self, temperature):
        print(f"TV Display updated: Temperature = {temperature}")

#client code
#publisher
weather = WeatherStation() 

#subscribers
phone = PhoneDisplay() 
tv = TVDisplay()

weather.attach(phone)
weather.attach(tv) 
weather.set_temperature(25)
weather.set_temperature(30)
#------------------------------------------------

#with above two interfaces publisher interface and subscriber interface
#we can make implement others like news update notifications.
#as Interfaces stay SAME
