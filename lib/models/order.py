from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base,session
from datetime import datetime

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id',ondelete='CASCADE'))
    customer_id = Column(Integer, ForeignKey('customers.id',ondelete='CASCADE'))
    order_date = Column(DateTime,default=datetime.utcnow)

    customer = relationship('Customer', back_populates='orders')
    product = relationship('Product', back_populates='orders')
    def __init__(self,product_id,customer_id,id=None):
    if isinstance(product_id,int) and isinstance(customer_id,int):
        self.product_id=product_id
        self.customer_id=customer_id
        self.order_date=datetime.utcnow()
    else:
        raise TypeError('customer id and product id must both be integers')
    def save_order(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_order_by_customer(cls , id):
        orders=session.query(cls).filter_by(customer_id=id).all()
        return [order for order in orders]
    @classmethod
    def get_all(cls):
        orders=session.query(cls).all()
        return [order for order in orders]
    @classmethod
    def delete_order(cls,id):
        order=session.query(cls).filter_by(id=id).first()
        session.delete(order)
        session.commit()
    def __repr__(self):
        date_str = self.order_date.strftime("%Y-%m-%d %H:%M:%S")
        return f"<order_id : {self.id},product_id:{self.product_id},customer_id:{self.customer_id},date_of_order:{date_str}>"

