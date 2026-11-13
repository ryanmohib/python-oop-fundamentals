
"""
BANK ACCOUNT MANAGEMENT SYSTEM
Concept: Encapsulation

A simple banking application that allows users to:
- Deposit money
- Withdraw money
- Check their balance

The account balance is protected using a private attribute.
"""


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        self.__balance += amount
        print(f"Successfully deposited: {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero!")

        elif amount > self.__balance:
            print("Insufficient balance!")

        else:
            self.__balance -= amount
            print(f"Successfully withdrawn: {amount:.2f}")

    def get_balance(self):
        return self.__balance


def main():

    print("=" * 35)
    print("       BANK ACCOUNT SYSTEM")
    print("=" * 35)

    owner = input("Enter account holder name: ").strip()

    if not owner:
        print("Name cannot be empty!")
        return

    account = BankAccount(owner)

    while True:

        print("=" * 35)
        print("\n1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":

            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":

            print(f"\nAccount holder: {account.owner}")
            print(f"Current balance: {account.get_balance():.2f}")

        elif choice == "4":

            print("=" * 35)
            print(f"Thank you {account.owner} for using our banking system!")
            break

        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
