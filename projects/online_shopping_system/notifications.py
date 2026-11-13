
from abc import ABC, abstractmethod


class NotificationInterface(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationInterface):

    def send(self, message):
        print("\n--- Email Notification ---")
        print(message)
        print("Email sent successfully!")
