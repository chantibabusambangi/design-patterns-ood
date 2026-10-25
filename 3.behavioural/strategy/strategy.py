from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#concrete strategyies/algorithms
#and say each strategy/algorihtms have different parameters to take
class CreditCardPayment(PaymentStrategy):
    def __init__(self,cardnumber, cvv):
        self.card_number=cardnumber
        self.cvv=cvv
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class PaypalPayment(PaymentStrategy):
    #lly here also it initialised with paramters required to make payment
    def __init__(self,paypal_id):
        self.paypal_id=paypal_id
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

class UpiPayment(PaymentStrategy):
    def __init__(self,upi_id):
        self.upi_id=upi_id
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
#context to make use of these strategies

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    def make_payment(self, amount):
        self.strategy.pay(amount)
#client code

payment = PaymentContext(CreditCardPayment(5258,955)) #payment is the paymentcontext
payment.make_payment(1000)
#one context is to be created and we use this only, and by setting other strategies.

payment.set_strategy(PaypalPayment(123))
payment.make_payment(2000)

payment.set_strategy(UpiPayment(1234))
payment.make_payment(500)
