
from abc import ABC, abstractmethod

# 1. Base class for all payment types
class IPayment(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def collect_payment(self):
        pass

# 2. Specialized interface for payments that require fraud checks
class IFraudCheckable(IPayment):
    @abstractmethod
    def run_fraud_check(self):
        pass

# --- Implementations ---

class CreditCard(IFraudCheckable):
    def validate(self): print("Validating...")
    def run_fraud_check(self): print("Checking fraud...")
    def collect_payment(self): print("Collecting...")

class RewardCard(IPayment): # Notice it does NOT inherit from IFraudCheckable
    def validate(self): print("Validating...")
    def collect_payment(self): print("Collecting rewards...")

# --- Usage ---

def process_secure_payment(payment: IFraudCheckable):
    payment.validate()
    payment.run_fraud_check() # Guaranteed to work and be meaningful
    payment.collect_payment()

def process_any_payment(payment: IPayment):
    payment.validate()
    payment.collect_payment()

#objects of parent class should be replaceble by objects of subclasses.
#if any class unable to implement any of method then it voilates liskov substitution principle.