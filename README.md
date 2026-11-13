
# 🐍 Python OOP Fundamentals

A collection of interactive Python applications and practical projects developed to understand and demonstrate the fundamental concepts of Object-Oriented Programming (OOP).

This repository contains five individual exercises, each focusing on a specific OOP concept, followed by a complete Online Shopping System that combines these concepts into a single application.

The goal is to strengthen my understanding of OOP through practical implementation, clean code organization, and interactive terminal-based applications.

---

## 📌 Table of Contents

- [About the Repository](#-about-the-repository)
- [OOP Concepts Covered](#-oop-concepts-covered)
- [Practical Exercises](#-practical-exercises)
  - [1. Encapsulation](#1-encapsulation--bank-account-management-system)
  - [2. Abstraction](#2-abstraction--animal-sound-system)
  - [3. Inheritance](#3-inheritance--employee-management-system)
  - [4. Polymorphism](#4-polymorphism--payment-processing-system)
  - [5. Interfaces](#5-interfaces--notification-management-system)
- [Final Project](#-final-project--online-shopping-system)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)
- [Learning Objectives](#-learning-objectives)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 About the Repository

Object-Oriented Programming is a programming paradigm based on organizing code into objects that combine data and behavior.

This repository was created as part of my journey to learn Python and understand how OOP principles are applied in real-world applications.

Rather than focusing only on theoretical explanations, each concept is demonstrated through a practical, interactive application where users can provide input and interact with the program through the terminal.

The repository progresses from individual exercises to a final project that combines multiple OOP principles into a more complete system.

---

## 🧠 OOP Concepts Covered

The repository focuses on the four fundamental pillars of Object-Oriented Programming, along with interfaces.

| Concept | Description |
|---|---|
| **Encapsulation** | Protecting data and controlling access to object attributes and methods. |
| **Abstraction** | Hiding implementation details and exposing essential functionality. |
| **Inheritance** | Reusing and extending functionality from existing classes. |
| **Polymorphism** | Allowing different objects to respond to the same method call in different ways. |
| **Interfaces** | Defining a common contract that classes must implement. |

---

## 💻 Practical Exercises

Each exercise is an independent, interactive Python application designed to demonstrate a specific OOP concept.

### 1. Encapsulation – Bank Account Management System

**File:** `exercises/01_encapsulation/bank_account.py`

A simple banking application that allows users to manage a bank account through an interactive terminal menu.

**Features:**
- Create a bank account.
- Deposit money.
- Withdraw money.
- Check the current balance.
- Validate transactions.

**OOP Implementation:**
- Uses a private attribute (`__balance`) to protect account data.
- Provides controlled access through methods.
- Demonstrates how encapsulation helps maintain data integrity.

### 2. Abstraction – Animal Sound System

**File:** `exercises/02_abstraction/animal_system.py`

An interactive application that allows users to select an animal and display its corresponding sound.

**Features:**
- Choose between different animals.
- Display the selected animal's sound.
- Handle invalid menu selections.

**OOP Implementation:**
- Uses an abstract `Animal` class.
- Defines an abstract `make_sound()` method.
- Requires subclasses to provide their own implementations.

### 3. Inheritance – Employee Management System

**File:** `exercises/03_inheritance/employee_management.py`

An employee management application that allows users to register employees and managers and display their information.

**Features:**
- Add regular employees.
- Add managers.
- Store employee information.
- Display all registered employees.
- Calculate total manager compensation, including bonuses.

**OOP Implementation:**
- Uses `Employee` as a parent class.
- Uses `Manager` as a child class.
- Demonstrates constructor inheritance using `super()`.
- Demonstrates method overriding.

### 4. Polymorphism – Payment Processing System

**File:** `exercises/04_polymorphism/payment_system.py`

A simple payment application that allows users to choose a payment method and simulate a transaction.

**Features:**
- Choose between Credit Card, PayPal, and Cash.
- Enter a custom payment amount.
- Simulate payment processing.
- Validate payment amounts.

**OOP Implementation:**
- Defines a common `pay()` method across different classes.
- Demonstrates how different objects implement the same method differently.
- Uses duck typing to achieve polymorphism without requiring a shared parent class.

### 5. Interfaces – Notification Management System

**File:** `exercises/05_interfaces/notification_system.py`

An interactive notification application that allows users to select a notification method and enter a custom message.

**Features:**
- Send simulated Email notifications.
- Send simulated SMS notifications.
- Send simulated Push notifications.
- Enter custom messages.
- Validate user input.

**OOP Implementation:**
- Defines an abstract `NotificationInterface` class.
- Uses an abstract `send()` method.
- Requires concrete notification classes to implement the same method.
- Demonstrates interface-like behavior using Python's Abstract Base Classes (`ABC`).

---

## 🚀 Final Project – Online Shopping System

In addition to the individual exercises, this repository includes a more complete project that combines multiple OOP concepts into one application.

**Project:** Online Shopping System

A command-line shopping application that simulates a basic online purchasing process.

**Features:**
- Product management.
- Add and remove products from a shopping cart.
- Calculate the total purchase price.
- Choose between different payment methods.
- Simulate payment processing.
- Send purchase confirmation notifications.

**OOP Concepts Applied:**

| Concept | Implementation |
|---|---|
| Encapsulation | Private product prices and shopping cart items. |
| Abstraction | Abstract `Payment` class. |
| Inheritance | Concrete payment classes inherit from `Payment`. |
| Polymorphism | Different payment methods implement `process_payment()`. |
| Interfaces | `NotificationInterface` defines the notification contract. |
| Composition | `ShoppingCart` contains `Product` objects. |

The project is organized into separate modules to improve readability, maintainability, and code reusability.

---

## 📁 Project Structure

```text
python-oop-fundamentals/
│
├── README.md
├── .gitignore
│
├── exercises/
│   │
│   ├── 01_encapsulation/
│   │   └── bank_account.py
│   │
│   ├── 02_abstraction/
│   │   └── animal_system.py
│   │
│   ├── 03_inheritance/
│   │   └── employee_management.py
│   │
│   ├── 04_polymorphism/
│   │   └── payment_system.py
│   │
│   └── 05_interfaces/
│       └── notification_system.py
│
└── projects/
    │
    └── online_shopping_system/
        │
        ├── README.md
        ├── main.py
        ├── product.py
        ├── shopping_cart.py
        ├── payments.py
        └── notifications.py
```

---

## 🛠️ Technologies Used

- **Python 3:** Main programming language.
- **Object-Oriented Programming:** Classes, objects, inheritance, encapsulation, abstraction, and polymorphism.
- **Abstract Base Classes (ABC):** Implementing abstract classes and interface-like contracts.
- **Git & GitHub:** Version control and project hosting.

No external Python libraries are required.

---

## ⚙️ Getting Started

### Prerequisites

Make sure Python 3 is installed on your machine.

Check your Python version:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/ryanmohib/python-oop-fundamentals.git
```

### 2. Navigate to the Project Directory

```bash
cd python-oop-fundamentals
```

### 3. Run an Exercise

Choose an exercise and execute its Python file.

**Encapsulation – Bank Account System**

```bash
python exercises/01_encapsulation/bank_account.py
```

**Abstraction – Animal Sound System**

```bash
python exercises/02_abstraction/animal_system.py
```

**Inheritance – Employee Management System**

```bash
python exercises/03_inheritance/employee_management.py
```

**Polymorphism – Payment Processing System**

```bash
python exercises/04_polymorphism/payment_system.py
```

**Interfaces – Notification Management System**

```bash
python exercises/05_interfaces/notification_system.py
```

### 4. Run the Final Project

Navigate to the Online Shopping System directory:

```bash
cd projects/online_shopping_system
```

Run the application:

```bash
python main.py
```

All applications are interactive and accept user input directly through the terminal.

---

## 🎯 Learning Objectives

Through these exercises and projects, I aim to:

- Understand the fundamental principles of Object-Oriented Programming.
- Learn how to design and organize classes and objects.
- Apply encapsulation to protect and manage data.
- Understand abstraction through abstract classes and methods.
- Practice inheritance and code reusability.
- Implement polymorphism through method overriding and duck typing.
- Understand interface-like structures in Python.
- Improve problem-solving and programming skills.
- Organize Python applications into multiple modules.
- Build practical applications using OOP principles.

---

## 🔮 Future Improvements

Some potential improvements and extensions for this repository include:

- Add automated unit tests using Python's `unittest` framework.
- Implement persistent data storage.
- Improve input validation and exception handling.
- Add more advanced OOP exercises.
- Extend the Online Shopping System with customer accounts and order history.
- Explore additional software design principles and design patterns.

---

## 👨‍💻 Author

**Rayan Mouhib**

Aspiring Python Developer | Learning Object-Oriented Programming

GitHub: [@ryanmohib](https://github.com/ryanmohib)

---

⭐ If you find this repository useful, feel free to explore the exercises and projects!
