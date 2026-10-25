#Clients should not be forced to implement unnecessary methods they do not use.

from abc import ABC, abstractmethod
class BurgerOrder(ABC):
    @abstractmethod
    def order_burger(self):
        pass
class FriesOrder(ABC):
    @abstractmethod
    def order_fries(self):
        pass
class ComboOrder(ABC):
    @abstractmethod
    def order_combo(self):
        pass
class BurgerOrderService(BurgerOrder):
    def order_burger(self):
        print("Ordering burger")

#if you full all methods use inheritance of all.
class FullMenuOrderService(BurgerOrder, FriesOrder, ComboOrder):
    def order_burger(self):
        print("Ordering burger")
    def order_fries(self):
        print("Ordering fries")
    def order_combo(self):
        print("Ordering combo")
#solved with interface segregation principle.