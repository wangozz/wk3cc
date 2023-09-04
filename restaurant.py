from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define the relationship to reviews
    reviews = relationship('Review', back_populates='restaurant')

    # Class method to find the fanciest restaurant
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    # Method to get all reviews for this restaurant
    def all_reviews(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [r.full_review() for r in reviews]
