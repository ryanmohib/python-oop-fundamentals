**Online Shopping System**
`Overview`

A command-line Online Shopping System built with Python to demonstrate the practical application of Object-Oriented Programming (OOP) principles.

The application allows users to browse products, add them to a shopping cart, calculate the total price, choose a payment method, and receive a purchase confirmation.

**Features**
Product management with price validation.
Encapsulated product prices using private attributes and properties.
Shopping cart management (add, remove, and calculate total).
Multiple payment methods (Credit Card and PayPal).
Abstract payment classes.
Polymorphic payment processing.
Notification system using an abstract interface.
Purchase confirmation after successful payment.
OOP Concepts Demonstrated
Concept	Implementation
Encapsulation	Private product price and cart items
Abstraction	Abstract Payment class
Inheritance	CreditCardPayment and PayPalPayment
Polymorphism	Different payment implementations
Interface	NotificationInterface using ABC
Project Structure
text
online_shopping_system/
├── main.py
├── product.py
├── shopping_cart.py
├── payments.py
├── notifications.py
└── README.md

**Technologies**
Python 3
Object-Oriented Programming
Abstract Base Classes (ABC)
How to Run
Clone the repository.
Navigate to the project directory.
Run:
bash
python main.py

Add products to the shopping cart through the application.
Select a payment method to complete the simulated purchase.
Learning Objectives

*This project was developed to practice designing classes, implementing OOP principles, organizing Python code into modules, and building a small application using reusable components.*

**Future Improvements**
Add customer accounts.
Add product quantities and stock management.
Implement order history.
Add unit tests.
Integrate a real payment provider in a future version.

Project status: Learning project – ongoing improvements.
