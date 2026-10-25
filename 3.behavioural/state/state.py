from abc import ABC, abstractmethod
#state Interface(state can have these actions)
class ATMState(ABC):
    @abstractmethod
    def insert_card(self): 
        pass
    @abstractmethod
    def enter_pin(self, pin): 
        pass
    @abstractmethod
    def withdraw_cash(self, amount):
        pass

#concrete states 1.NO card state, 2.has card state 3.authenticated state 4.out of cash state.
class NoCardState(ATMState):
    def __init__(self, atm): 
        self.atm = atm
    def insert_card(self):
        print("Card inserted.")
        self.atm.set_state(self.atm.has_card_state)
    def enter_pin(self, pin):
        print("Insert card first.")
    def withdraw_cash(self, amount): 
        print("Insert card first.")

class HasCardState(ATMState):
    def __init__(self, atm): 
        self.atm = atm
    def insert_card(self): 
        print("Card already inside.")
    def enter_pin(self, pin):
        if pin == 1234:
            print("PIN correct.")
            self.atm.set_state(self.atm.authenticated_state)
        else:
            print("Wrong PIN. Card ejected.")
            self.atm.set_state(self.atm.no_card_state)
    def withdraw_cash(self, amount): 
        print("Enter PIN first.")

class AuthenticatedState(ATMState):
    def __init__(self, atm): 
        self.atm = atm
    def insert_card(self): 
        print("Transaction in progress.")
    def enter_pin(self, pin): 
        print("Already authenticated.")
    def withdraw_cash(self, amount):
        if amount > self.atm.balance:
            print("Insufficient balance!")
        else:
            self.atm.balance -= amount
            print(f"Withdrawn {amount}. Remaining: {self.atm.balance}")
            if self.atm.balance <= 0:
                self.atm.set_state(self.atm.out_of_cash_state)
            else:
                self.atm.set_state(self.atm.no_card_state)

class OutOfCashState(ATMState):
    def __init__(self, atm): 
        self.atm = atm
    def insert_card(self): 
        print("Machine out of cash. Try another ATM.")
    def enter_pin(self, pin): 
        print("Machine empty.")
    def withdraw_cash(self, amount): 
        print("Machine empty.")
#context ATMMachine
class ATM:
    def __init__(self, balance=5000):
        self.balance = balance
        # Pre-initialize states (Singleton-like behavior)
        #this step reduces gargabage collections, prevents everytime we use new object. #this is very very important, avoid creating new state objects everytime.
        #imprvement1
        self.no_card_state = NoCardState(self)
        self.has_card_state = HasCardState(self)
        self.authenticated_state = AuthenticatedState(self)
        self.out_of_cash_state = OutOfCashState(self)
        
        self.state = self.no_card_state

    def set_state(self, state):
        self.state = state

    def insert_card(self): 
        self.state.insert_card()
    def enter_pin(self, pin):
        self.state.enter_pin(pin)
    def withdraw_cash(self, amount):
        self.state.withdraw_cash(amount)
    def add_cash(self,cash): #this is optinal
        self.balance+=cash
        #update the state if it was outof-cash state
        if(self.state is self.out_of_cash_state and self.balance>0):
            self.set_state(self.no_card_state)
#client code
atm=ATM() #atm machine have 5k cash.

atm.insert_card()
atm.enter_pin(1234)
atm.withdraw_cash(1000)
atm.withdraw_cash(1000)