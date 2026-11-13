
"""
NOTIFICATION MANAGEMENT SYSTEM
OOP Concept: Interface

Features:
- Choose a notification method.
- Enter a custom message.
- Send Email, SMS, or Push Notifications.
- Enforce a common send() method using ABC.

How to run:
python notification_system.py
"""

from abc import ABC, abstractmethod


class NotificationInterface(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationInterface):

    def send(self, message):
        print("\nSending Email...")
        print(f"Email content: {message}")
        print("Email sent successfully!")


class SMSNotification(NotificationInterface):

    def send(self, message):
        print("\nSending SMS...")
        print(f"SMS content: {message}")
        print("SMS sent successfully!")


class PushNotification(NotificationInterface):

    def send(self, message):
        print("\nSending Push Notification...")
        print(f"Notification content: {message}")
        print("Push notification sent successfully!")


def main():

    notifications = {
        "1": ("Email", EmailNotification()),
        "2": ("SMS", SMSNotification()),
        "3": ("Push Notification", PushNotification())
    }

    while True:

        print("\n===== NOTIFICATION SYSTEM =====")
        print("1. Email")
        print("2. SMS")
        print("3. Push Notification")
        print("4. Exit")

        choice = input("\nChoose notification method: ").strip()

        if choice == "4":
            print("Exiting notification system!")
            break

        elif choice in notifications:

            message = input("Enter your message: ").strip()

            if not message:
                print("Message cannot be empty!")
                continue

            name, notification = notifications[choice]

            notification.send(message)

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
