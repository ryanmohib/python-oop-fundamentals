
from product import Product
from shopping_cart import ShoppingCart
from payments import CreditCardPayment, PayPalPayment
from notifications import EmailNotification


def main():

    # 1. Create products
    laptop = Product("Laptop", 1000)
    phone = Product("Phone", 500)

    # 2. Create shopping cart
    cart = ShoppingCart()

    # 3. Add products
    cart.add_product(laptop)
    cart.add_product(phone)

    # 4. Display cart and calculate total
    cart.display_cart()

    total = cart.calculate_total()

    # 5. Choose payment method
    print("\nChoose your payment method:")
    print("1. Credit Card")
    print("2. PayPal")

    choice = input("Your choice: ")

    if choice == "1":
        payment = CreditCardPayment()

    elif choice == "2":
        payment = PayPalPayment()

    else:
        print("Invalid payment method!")
        return

    # 6. Process payment
    success = payment.process_payment(total)

    # 7. Send notification if successful
    if success:
        notification = EmailNotification()

        notification.send(
            f"Your order was successful! Total paid: {total}"
        )


if __name__ == "__main__":
    main()
