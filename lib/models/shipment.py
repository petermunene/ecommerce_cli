from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base,session

class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    shipment_date = Column(DateTime)
    shipment_type = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id',ondelete='CASCADE'))

    customer = relationship('Customer', back_populates='shipments')
    shipment_options=[delivery,personal management]
    def __init__(self,shipment_date,shipment_type,customer_id,id=None):
    if shipment_type in shipment_options and isinstance(customer_id,int):
        self.shipment_date=shipment_date
        self.shipment_type=shipment_type
        self.customer_id=customer_id
        self.id=id
    else:
        raise TypeError("Invalid shipment type or customer_id")
    def save_shipment(self):
        session.add(self)
        session.commit()
    @classmethod
    def get_all(cls):
        shipments=session.query(cls).all()
        return [shipment for shipment in shipments]
    def __repr__(self):
        return f"<id:{self.id}| shipment_date:{self.shipment_date}| shipment_type:{self.shipment_type}| customer_id:{self.customer_id}>"
    @classmethod
    def get_by_customer_id(cls,id):
        shipments=session.query(cls).filter_by(customer_id=id).all()
        return [shipment for shipment in shipments]
