from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(Text, nullable=True)
    phone_no = Column(Text, nullable=False) 
    # Relationships
    orders = relationship('Order', back_populates='customer')
    shipments = relationship('Shipment', back_populates='customer')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime)

    # Relationships
    customer = relationship('Customer', back_populates='orders')
    product = relationship('Product', back_populates='orders')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    owner_id = Column(Integer, ForeignKey('product_owners.id'))

    # Relationships
    owner = relationship('Product_owner', back_populates='products')
    orders = relationship('Order', back_populates='product')


class ProductOwner(Base):
    __tablename__ = 'product_owners'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship
    products = relationship('Product', back_populates='owner')


class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    shipment_date = Column(DateTime)
    shipment_type = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Relationship
    customer = relationship('Customer', back_populates='shipments')