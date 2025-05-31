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
        print("10. Delete Customer by ID")
        print("11. Back to Role Selection")

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
                print(f"Name: {c['name']}, Email: {c['email']}, Phone: {c['phone_no']}")

        elif choice == '3':
            try:
                id = int(input("Enter customer ID: "))
                customer = Customer.find_customer_by_id(id)
                if customer:
                    print(f"Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone_no}")
                else:
                    print("Customer not found.")
            except ValueError:
                print("Invalid ID. Make sure ID is a number.")

        elif choice == '4':
            try:
                product_id = int(input("Enter product ID to order: "))
                customer_id = int(input("Enter your customer ID: "))
                order = Order(product_id=product_id, customer_id=customer_id)
                order.save_order()
                print("Order placed successfully!")
            except ValueError:
                print("Invalid input. Make sure product ID and customer ID are both numbers.")

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
                customer_id = int(input("Customer ID: "))
                shipment_type = input("Shipment Type (delivery/personal management): ").lower()
                shipment_date = datetime.now()
                shipment = Shipment(shipment_date=shipment_date, shipment_type=shipment_type, customer_id=customer_id)
                shipment.save_shipment()
                print("Shipment added!")
            except Exception as e:
                print("Error adding shipment:", e)

        elif choice == '8':
            try:
                customer_id = int(input("Customer ID: "))
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
            try:
                customer_id = int(input("Enter customer ID to delete: "))
                Customer.delete_customer(customer_id)
                print("Customer deleted.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '11':
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
        print("5. Add Product Owner")
        print("6. View All Product Owners")
        print("7. View Product Owner by ID")
        print("8. Delete Product Owner by ID")
        print("9. Back to Role Selection")

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
                if Product.delete(product_id):
                    print("Product deleted.")
                else:
                    print("Product not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '5':
            name = input("Enter owner name: ")
            try:
                owner = ProductOwner(name=name)
                owner.save_owner()
                print("Product owner added.")
            except Exception as e:
                print("Error adding owner:", e)

        elif choice == '6':
            owners = ProductOwner.get_all()
            for o in owners:
                print(o)

        elif choice == '7':
            try:
                id = int(input("Enter owner ID: "))
                owner = ProductOwner.get_by_id(id)
                if owner:
                    print(owner)
                else:
                    print("Owner not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '8':
            try:
                id = int(input("Enter owner ID to delete: "))
                ProductOwner.delete_owner(id)
                print("Product owner deleted.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '9':
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