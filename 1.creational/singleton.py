from threading import Lock
#Python executes __new__ first, then __init__.
class Singleton:#we want only one object of this class.
    instance = None #class variable
    lock = Lock() #class variable
    #mutex lock,we want to ensure one thread creates instance.
    
    def __new__(cls):
        if cls.instance is None: #to makesure lock acquired at first time(instance created time) only
            with cls.lock:
                if(cls.instance is None):
                    cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        if not hasattr(self,"initialized"):#class varibale can also accessed with self
            self.path="file_path"
            self.name="data center"
            self.val=10
            self.initialized=True #updating class variable
    from threading import Lock



    def some_business_logic(self):
        print("Business logic executed")
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)   # True
print(s1.path,s1.name,s1.val)
s1.some_business_logic()
#class varible can be access with self if you have any object of it.
#cons: makes unit testing difficult and harder.