
"""
EMPLOYEE MANAGEMENT SYSTEM
Concept: Inheritance

Users can create employees and managers,
display their information, and manage employee records.

Manager inherits common attributes and methods
from the Employee parent class.
"""


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):

        print(f"\nName: {self.name}")
        print(f"Position: Employee")
        print(f"Salary: {self.salary:.2f}")


class Manager(Employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display_info(self):

        print(f"\nName: {self.name}")
        print(f"Position: Manager")
        print(f"Salary: {self.salary:.2f}")
        print(f"Bonus: {self.bonus:.2f}")
        print(f"Total compensation: {self.salary + self.bonus:.2f}")


def main():

    employees = []

    print("=" * 35)
    print("    EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 35)

    while True:

        print("\n1. Add Employee")
        print("2. Add Manager")
        print("3. Display All Employees")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            name = input("Employee name: ").strip()

            try:
                salary = float(input("Employee salary: "))

                if not name or salary < 0:
                    print("Invalid name or salary!")
                    continue

                employee = Employee(name, salary)
                employees.append(employee)

                print("Employee added successfully!")

            except ValueError:
                print("Please enter a valid salary!")

        elif choice == "2":

            name = input("Manager name: ").strip()

            try:
                salary = float(input("Manager salary: "))
                bonus = float(input("Manager bonus: "))

                if not name or salary < 0 or bonus < 0:
                    print("Invalid information!")
                    continue

                manager = Manager(name, salary, bonus)
                employees.append(manager)

                print("Manager added successfully!")

            except ValueError:
                print("Please enter valid numbers!")

        elif choice == "3":

            if not employees:
                print("No employees registered yet!")

            else:
                print("\n===== EMPLOYEE RECORDS =====")

                for employee in employees:
                    employee.display_info()
                    print("-" * 30)

        elif choice == "4":

            print("Exiting employee management system!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
