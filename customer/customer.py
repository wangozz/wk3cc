
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('wk3cc.review.review.Review', back_populates='customer')
    restaurants = relationship('wk3cc.restaurant.restaurant.Restaurant', secondary='wk3cc.review.review.Review', back_populates='customers')
