
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('wk3cc.restaurant.restaurant.id'))
    customer_id = Column(Integer, ForeignKey('wk3cc.customer.customer.id'))
    restaurant = relationship('wk3cc.restaurant.restaurant.Restaurant', back_populates='reviews')
    customer = relationship('wk3cc.customer.customer.Customer', back_populates='reviews')
