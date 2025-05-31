# E-Commerce CLI Management System
A command-line interface (CLI) based backend system for managing an e-commerce platform. This system supports product and customer management, order processing, shipment tracking, and ownership records — all managed via a simple terminal interface using SQLAlchemy and SQLite/MySQL.

# Features
# Product Owner Management
Create and save new product owners with name validation.

List all product owners.

Delete product owners by ID.

# Product Management
Add products with validation on name length and ownership.

List all available products.

Get products by owner ID.

Delete products by ID.

# Customer Management
Create customers with validation for name and email format.

List all customers with details (name, email, phone number).

Find customers by ID or name.

Delete customers by ID.

# Order Management
Create and save orders (requires valid customer and product IDs).

List all orders.

List orders by customer ID.

Delete orders by ID.

# Shipment Management
Create and save shipments with type and customer ID validation.

Supported shipment types: delivery, personal management.

List all shipments.

Get shipments by customer ID.

# How to Use
open the  cli in terminal and run the cli.py file .
you will be prompted with commands to execute commands depending on your needs .



# Validation & Error Handling
Owner and product names must be strings and 1–25 characters long.

Product and customer IDs must be integers.

Emails must contain @.

Shipment types are restricted to delivery and personal management.