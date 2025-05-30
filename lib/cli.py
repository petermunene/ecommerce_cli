from database import Base, engine
from models import Product, ProductOwner, Order, Customer, Shipment
Base.metadata.create_all(engine)
import sys
from datetime import datetime

def customer_menu():
    while True:
        print("\n=== Customer Menu ===")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Find Customer by ID")
        print("4. Place Order")
        print("5. View Orders by Customer ID")
        print("6. View All Orders")
        print("7. Add Shipment")
        print("8. View Shipments by Customer ID")
        print("9. View All Shipments")
        print("10. Back to Role Selection")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone number: ")
            customer = Customer(name=name, email=email, phone_no=phone)
            customer.save_customer()
            print("Customer added!")

        elif choice == '2':
            customers = Customer.get_all()
            for c in customers:
                print(c)

        elif choice == '3':
            try:
                id = int(input("Enter customer ID: "))
                customer = Customer.find_customer_by_id(id)
                if customer:
                    print(f"Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone_no}")
                else:
                    print("Customer not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '4':
            try:
                product_id = int(input("Enter product ID to order: "))
                customer_id = int(input("Enter your customer ID: "))
                order = Order(product_id=product_id, customer_id=customer_id)
                order.save_order()
                print("Order placed successfully!")
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            try:
                customer_id = int(input("Enter your customer ID: "))
                orders = Order.get_order_by_customer(customer_id)
                for o in orders:
                    print(o)
            except ValueError:
                print("Invalid ID.")

        elif choice == '6':
            orders = Order.get_all()
            for o in orders:
                print(o)

        elif choice == '7':
            try:
                customer_id = int(input("Enter your customer ID: "))
                shipment_type = input("Enter shipment type (delivery/personal management): ")
                shipment_date = datetime.utcnow()
                shipment = Shipment(shipment_date=shipment_date, shipment_type=shipment_type, customer_id=customer_id)
                shipment.save_shipment()
                print("Shipment added!")
            except ValueError:
                print("Invalid ID.")

        elif choice == '8':
            try:
                customer_id = int(input("Enter your customer ID: "))
                shipments = Shipment.get_by_customer_id(customer_id)
                for s in shipments:
                    print(s)
            except ValueError:
                print("Invalid ID.")

        elif choice == '9':
            shipments = Shipment.get_all()
            for s in shipments:
                print(s)

        elif choice == '10':
            return

        else:
            print("Invalid option. Please try again.")

def product_owner_menu():
    while True:
        print("\n=== Product Owner Menu ===")
        print("1. Add Product")
        print("2. View All Products")
        print("3. View Products by Owner ID")
        print("4. Delete Product by ID")
        print("5. Back to Role Selection")
        choice = input("Select an option: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            try:
                owner_id = int(input("Enter your owner ID: "))
                product = Product(product_name=product_name, owner_id=owner_id)
                product.save()
                print("Product added.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '2':
            products = Product.get_all()
            for p in products:
                print(f"ID: {p.id}, Name: {p.product_name}, Owner ID: {p.owner_id}")

        elif choice == '3':
            try:
                owner_id = int(input("Enter owner ID: "))
                products = Product.get_product_by_owner_id(owner_id)
                for p in products:
                    print(f"ID: {p.id}, Name: {p.product_name}")
            except ValueError:
                print("Invalid ID.")

        elif choice == '4':
            try:
                product_id = int(input("Enter product ID to delete: "))
                Product.delete(product_id)
                print("Product deleted.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '5':
            return

        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("\n=== Login Role Selection ===")
        print("1. Customer")
        print("2. Product Owner")
        print("3. Exit")
        role = input("Select your role: ")

        if role == '1':
            customer_menu()
        elif role == '2':
            product_owner_menu()
        elif role == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please choose again.")

if __name__ == "__main__":
    main()