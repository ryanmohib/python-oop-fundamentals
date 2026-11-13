
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):

    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount!")
            return False

        print(f"Processing Credit Card payment: {amount}")
        print("Credit Card payment successful!")

        return True


class PayPalPayment(Payment):

    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount!")
            return False

        print(f"Processing PayPal payment: {amount}")
        print("PayPal payment successful!")

        return True
