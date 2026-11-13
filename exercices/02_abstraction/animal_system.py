
"""
ANIMAL SOUND SYSTEM
Concept: Abstraction

Users can choose an animal and hear its sound.

The abstract Animal class defines a common method
that every animal must implement.
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):

    def make_sound(self):
        return "Meow!"


class Cow(Animal):

    def make_sound(self):
        return "Moooo!"


class Duck(Animal):

    def make_sound(self):
        return "Quack! Quack!"


def main():

    animals = {
        "1": ("Dog", Dog()),
        "2": ("Cat", Cat()),
        "3": ("Cow", Cow()),
        "4": ("Duck", Duck())
    }

    print("=" * 35)
    print("       ANIMAL SOUND SYSTEM")
    print("=" * 35)

    while True:

        print("\nChoose an animal:")

        for number, (name, animal) in animals.items():
            print(f"{number}. {name}")

        print("5. Exit")

        choice = input("\nYour choice: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        elif choice in animals:

            name, animal = animals[choice]

            print(f"\nYou selected: {name}")
            print(f"Sound: {animal.make_sound()}")

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
