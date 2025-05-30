from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base, session

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(Text, nullable=True)
    phone_no = Column(Text, nullable=False)

    orders = relationship('Order', back_populates='customer',cascade='all,delete-orphan')
    shipments = relationship('Shipment', back_populates='customer',cascade='all,delete-orphan')

    def __init__(self, name, email, phone_no, id=None):
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.id = id

    def save_customer(self):
        session.add(self)
        session.commit()

    @classmethod
    def find_customer_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    @classmethod
    def delete_customer(cls,id):
        customer=session.query(cls).filter_by(id=id).first()
        session.delete(customer)
        session.commit()
    @classmethod
    def get_all(cls):
        customers = session.query(cls).all()
        return [
            {
                "name": customer.name,
                "email": customer.email,
                "phone_no": customer.phone_no
            }
            for customer in customers
        ]

    @classmethod
    def find_customer_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

        
