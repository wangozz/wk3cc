from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define the relationship to reviews
    reviews = relationship('Review', back_populates='customer')

    # Method to get the full name of the customer
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # Method to find the favorite restaurant of the customer
    def favorite_restaurant(self):
        reviews = session.query(Review).filter_by(customer_id=self.id)
        favorite = max(reviews, key=lambda r: r.star_rating, default=None)
        return favorite.restaurant if favorite else None

    # Method to add a review for a restaurant
    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(review)
        session.commit()

    # Method to delete all reviews for a restaurant
    def delete_reviews(self, restaurant):
        session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant.id).delete()
        session.commit()
