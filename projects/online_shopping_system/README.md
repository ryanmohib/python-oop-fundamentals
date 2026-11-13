
# 🛒 Online Shopping System

A command-line Online Shopping System built with Python to demonstrate the practical application of Object-Oriented Programming (OOP) principles.

The application allows users to browse available products, add and remove products from a shopping cart, calculate the total price, choose a payment method, and receive a purchase confirmation.

This project brings together several OOP concepts in a single application, focusing on code organization, reusability, encapsulation, and modular design.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [OOP Concepts Demonstrated](#-oop-concepts-demonstrated)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)
- [How to Use](#-how-to-use)
- [Learning Objectives](#-learning-objectives)
- [Future Improvements](#-future-improvements)
- [Project Status](#-project-status)

---

## 📖 Overview

The Online Shopping System simulates a basic purchasing process through an interactive terminal interface.

Users can explore products, manage their shopping cart, review the total purchase price, and select a payment method to complete a simulated transaction.

The application is organized into multiple Python modules, with each module responsible for a specific part of the system.

The main purpose of this project is to apply the fundamental principles of Object-Oriented Programming in a practical and structured application.

---

## ✨ Features

- 🛍️ **Product Management:** Browse available products and their prices.
- 🔒 **Encapsulated Product Prices:** Protect product prices using private attributes and properties.
- 🛒 **Shopping Cart Management:** Add and remove products from the shopping cart.
- 💰 **Price Calculation:** Automatically calculate the total purchase price.
- 💳 **Multiple Payment Methods:** Choose between Credit Card and PayPal.
- 🧩 **Abstract Payment Classes:** Define a common payment structure using abstract classes.
- 🔄 **Polymorphic Payment Processing:** Implement different payment behaviors through a common method.
- 📩 **Notification System:** Use an abstract notification interface.
- ✅ **Purchase Confirmation:** Receive a confirmation notification after a successful simulated payment.

---

## 🧠 OOP Concepts Demonstrated

This project combines the main Object-Oriented Programming principles into a single application.

| Concept | Implementation |
|---|---|
| **Encapsulation** | Private product prices and shopping cart items. |
| **Abstraction** | Abstract `Payment` class defining the payment structure. |
| **Inheritance** | `CreditCardPayment` and `PayPalPayment` inherit from `Payment`. |
| **Polymorphism** | Different payment classes implement their own `process_payment()` method. |
| **Interfaces** | `NotificationInterface` defines a common notification contract using ABC. |
| **Composition** | `ShoppingCart` manages `Product` objects. |

### 🔍 How the Concepts Work Together

- **Encapsulation:** Product prices and shopping cart data are protected and accessed through controlled methods.
- **Abstraction:** The abstract `Payment` class defines the required payment functionality without specifying the implementation.
- **Inheritance:** Concrete payment classes reuse the structure defined by the parent `Payment` class.
- **Polymorphism:** Different payment methods respond to the same `process_payment()` call with their own implementations.
- **Interfaces:** The notification classes follow a common contract by implementing the required `send()` method.

---

## 📁 Project Structure

```text
online_shopping_system/
│
├── README.md
│
├── main.py
├── product.py
├── shopping_cart.py
├── payments.py
└── notifications.py
```

### 📂 File Descriptions

| File | Responsibility |
|---|---|
| `main.py` | Main application entry point and user interaction. |
| `product.py` | Defines the Product class and manages product information. |
| `shopping_cart.py` | Handles shopping cart operations and total price calculation. |
| `payments.py` | Defines the abstract Payment class and concrete payment methods. |
| `notifications.py` | Defines the notification interface and notification implementations. |

---

## 🛠️ Technologies Used

- **Python 3:** Main programming language.
- **Object-Oriented Programming:** Classes, objects, encapsulation, abstraction, inheritance, and polymorphism.
- **Abstract Base Classes (ABC):** Implementing abstract classes and interface-like contracts.
- **Properties:** Managing controlled access to object attributes.
- **Git & GitHub:** Version control and project hosting.

No external Python libraries are required.

---

## ⚙️ Getting Started

### 📋 Prerequisites

Make sure Python 3 is installed on your machine.

Check your Python version:

```bash
python --version
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ryanmohib/python-oop-fundamentals.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd python-oop-fundamentals/projects/online_shopping_system
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🛍️ How to Use

Once the application starts, interact with the terminal to complete the shopping process.

1. Browse the available products.
2. Select products to add to your shopping cart.
3. Remove products if needed.
4. Review your shopping cart and total price.
5. Choose a payment method (Credit Card or PayPal).
6. Complete the simulated payment.
7. Receive a purchase confirmation notification.

**Note:** Payments and notifications are simulated. The application does not connect to real payment providers or external notification services.

---

## 🎯 Learning Objectives

This project was developed to practice:

- Designing and organizing Python classes and objects.
- Applying the fundamental principles of Object-Oriented Programming.
- Protecting data through encapsulation and properties.
- Implementing abstraction using abstract classes.
- Reusing functionality through inheritance.
- Understanding polymorphism through method overriding.
- Defining interface-like structures using Abstract Base Classes.
- Organizing Python applications into multiple modules.
- Building reusable and maintainable application components.
- Combining different OOP concepts in a practical project.

---

## 🚀 Future Improvements

Potential improvements and extensions for this project include:

- 👤 Add customer accounts and user authentication.
- 📦 Implement product quantities and stock management.
- 📜 Add order history and transaction records.
- 🧪 Implement automated unit tests using `unittest`.
- 💾 Add persistent data storage using a database.
- 💳 Integrate a real payment provider in a future version.
- 📧 Implement actual email notifications.

---

## 📌 Project Status

**Status:** Learning project – ongoing improvements.

This project is part of my Python OOP learning journey and serves as a practical demonstration of how Object-Oriented Programming principles can be combined to build a structured application.

---

⭐ Thanks for checking out this project!
