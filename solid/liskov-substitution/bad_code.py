
class IPayment:
    def validate(self):
        pass
    def run_fraud_check(self):
        pass
    def collect_payment(self):
        pass
#credit card and debit are made from this class.
class CreditCard(IPayment):
    def validate(self):
        print("Validating credit card")
    def run_fraud_check(self):
        print("Running fraud check")
    def collect_payment(self):
        print("Collecting credit card payment")
class DebitCard(IPayment):
    def validate(self):
        print("Validating debit card")
    def run_fraud_check(self):
        print("Running fraud check")
    def collect_payment(self):
        print("Collecting debit card payment")

#lets say we want to new card like rewards card. rewards card wont have run_fraud_check.
class RewardCard(IPayment):
    def validate(self):
        print("Validating reward card")
    def run_fraud_check(self):
        pass   # ❌ meaningless / fake implementation
    def collect_payment(self):
        print("Collecting reward card payment")
#Why this is bad: * Any system that processes IPaymentInstrument 
# will crash if it calls run_fraud_check on a RewardCard


#voilates LSP : cannot substitute safely.
#so we keep only two methods in IPayment

#solved by splitting the interfaces(interface segregation principle)

#The Liskov Substitution Principle (LSP) is about ensuring that a 
#subclass doesn't break the expectations set by its parent class.