
"""
PAYMENT PROCESSING SYSTEM
OOP Concept: Polymorphism

Features:
- Choose a payment method.
- Enter a payment amount.
- Process payments using different classes.
- Use the same method name with different implementations.

How to run:
python payment_system.py
"""


class CreditCard:

    def pay(self, amount):
        print("\nProcessing Credit Card payment...")
        print(f"Paid {amount:.2f} using Credit Card!")


class PayPal:

    def pay(self, amount):
        print("\nProcessing PayPal payment...")
        print(f"Paid {amount:.2f} using PayPal!")


class Cash:

    def pay(self, amount):
        print("\nProcessing Cash payment...")
        print(f"Paid {amount:.2f} using Cash!")


def main():

    payment_methods = {
        "1": ("Credit Card", CreditCard()),
        "2": ("PayPal", PayPal()),
        "3": ("Cash", Cash())
    }

    while True:

        print("\n===== PAYMENT SYSTEM =====")
        print("1. Credit Card")
        print("2. PayPal")
        print("3. Cash")
        print("4. Exit")

        choice = input("\nChoose payment method: ").strip()

        if choice == "4":
            print("Thank you!")
            break

        elif choice in payment_methods:

            try:
                amount = float(input("Enter payment amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero!")
                    continue

                name, payment = payment_methods[choice]

                payment.pay(amount)

            except ValueError:
                print("Please enter a valid amount!")

        else:
            print("Invalid payment method!")


if __name__ == "__main__":
    main()
