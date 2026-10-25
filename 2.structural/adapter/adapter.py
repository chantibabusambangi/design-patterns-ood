#Adapter is a structural design pattern that allows 
# collaboration of objects with incompatible interfaces.

from abc import ABC, abstractmethod


# ==========================
# Target Interface
# ==========================
class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# ==========================
# Third-Party SDKs (Adaptees)
# We cannot modify these classes.
# ==========================
class Stripe:

    def make_payment(self, amount):
        print(f"Stripe: Paid ${amount}")


class PayPal:

    def send_payment(self, amount):
        print(f"PayPal: Paid ${amount}")


class Razorpay:

    def process_payment(self, amount):
        print(f"Razorpay: Paid ${amount}")


# ==========================
# Adapters
# ==========================
class StripeAdapter(PaymentGateway):

    def __init__(self, stripe: Stripe):
        self.stripe = stripe

    def pay(self, amount):
        self.stripe.make_payment(amount)


class PayPalAdapter(PaymentGateway):

    def __init__(self, paypal: PayPal):
        self.paypal = paypal

    def pay(self, amount):
        self.paypal.send_payment(amount)


class RazorpayAdapter(PaymentGateway):

    def __init__(self, razorpay: Razorpay):
        self.razorpay = razorpay

    def pay(self, amount):
        self.razorpay.process_payment(amount)


# ==========================
# Client
# ==========================
class Checkout:

    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def checkout(self, amount):
        self.gateway.pay(amount)


# ==========================
# Client Code
# ==========================
stripe_gateway = StripeAdapter(Stripe())
paypal_gateway = PayPalAdapter(PayPal())
razorpay_gateway = RazorpayAdapter(Razorpay())

checkout = Checkout(stripe_gateway)
checkout.checkout(100)

checkout = Checkout(paypal_gateway)
checkout.checkout(250)

checkout = Checkout(razorpay_gateway)
checkout.checkout(500)