#Chain of Responsibility is a design pattern where a request is passed through a chain of handlers 
# until one handler processes it or the end of the chain is reached.

#1. Decouples sender and receiver ✅
#2.easy to extend (open-closed principle)✅, 3.single resonsibility principle✅ 4.flexible chain ✅,
from abc import ABC, abstractmethod
import random


class Handler(ABC):

    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler 

    def work_request(self):
        if self.can_handle():
            self.handle()
        elif self.next_handler:
            self.next_handler.work_request()
        else:
            print("Request failed.")

    @abstractmethod
    def can_handle(self):
        pass

    @abstractmethod
    def handle(self):
        pass


class Level1(Handler):

    def can_handle(self):
        return random.choice([True, False])

    def handle(self):
        print("Request handled by Level 1")


class Level2(Handler):

    def can_handle(self):
        return random.choice([True, False])

    def handle(self):
        print("Request handled by Level 2")


class Level3(Handler):

    def can_handle(self):
        return random.choice([True, False])

    def handle(self):
        print("Request handled by Level 3")


# Client

l1 = Level1()
l2 = Level2()
l3 = Level3()

l1.set_next(l2)
l2.set_next(l3)

for _ in range(10):
    l1.work_request()
    print("-" * 30)