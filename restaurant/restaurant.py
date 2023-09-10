
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('wk3cc.review.review.Review', back_populates='restaurant')
    customers = relationship('wk3cc.customer.customer.Customer', secondary='wk3cc.review.review.Review', back_populates='restaurants')
