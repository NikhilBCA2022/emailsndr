from abc import ABC, abstractmethod

# Abstract class
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Payment class
class Payment:
    def __init__(self, amount, payment_type):
        self.amount = amount
        self.payment_type = payment_type

class payment_options(Payment):
        def upi(self):
            print("UPI payment selected")
            print("Processing UPI payment of amount:", self.amount)

        def debit(self):
            print("Debit card payment selected")
            print("Processing debit card payment of amount:", self.amount)

        def credit(self):
            print("Credit card payment selected")
            print("Processing credit card payment of amount:", self.amount)

        def netbanking(self):
            print("Net banking payment selected")
            print("Processing net banking payment of amount:", self.amount)


pay=payment_options(1000, "UPI")
pay.upi()