from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base,session

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    owner_id = Column(Integer, ForeignKey('product_owners.id',ondelete='CASCADE') )

    owner = relationship('ProductOwner', back_populates='products')
    orders = relationship('Order', back_populates='product',cascade='all,delete-orphan')
    def __init__(self,product_name,owner_id,id=None):
        if isinstance (product_name,str) and (0<len(name)=<25):
            self.id=id
            self.product_name=product_name
        else:
            raise TypeError("product name must be string between 0 and 25 characters")
        if isinstance (owner_id,int):
            self.owner_id=owner_id
        else:
            raise TypeError("owner id must be a string .")
    def save(self):
        session.add(self)
        session.commit()
    @classmethod
    def get_product_by_owner_id(cls,id):
        products=session.query(cls).filter_by(owner_id=id).all()
        return[product for product in products]
    @classmethod
    def get_all(cls):
        products=session.query(cls).all()
        return [product for product in products]
    def __repr__(self):
        return f"<product_id : {self.id},product_name:{self.product_name},owner_id:{self.owner_id}>"
    @classmethod
    def delete(cls,id):
        product=session.query(cls).filter_by(id=id).first()
        session.delete(product)
        session.delete(delete)