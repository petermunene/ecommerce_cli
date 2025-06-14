from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base,session

class ProductOwner(Base):
    __tablename__ = 'product_owners'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    products = relationship('Product', back_populates='owner', cascade='all,delete-orphan' )
    def __init__(self,name,id=None):
        if all(part.isalpha() for part in name.split()) and (0<len(name)<=25):
            self.name=name
        else:
            raise ValueError("name must be string between 0 and 25 characters")
    def save_owner(self):
        session.add(self)
        session.commit()
    @classmethod
    def get_all(cls):
        owners=session.query(cls).all()
        return [owner for owner in owners]
    @classmethod
    def get_by_id(cls,id):
        owner=session.query(cls).filter_by(id=id).first()
        return owner 

    @classmethod
    def delete_owner(cls,id):
        owner=session.query(cls).filter_by(id=id).first()
        if owner:
            session.delete(owner)
            session.commit()
        else:
            None
    def __repr__(self):
        return f"<owner_id:{self.id},name:{self.name}>"
        

