from .table_set_up import Customer
from sqlalchemy.orm import sessionmaker, create_engine

engine = create_engine("sqlite:///ecommerce.db")