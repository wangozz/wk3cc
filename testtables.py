from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', backref='reviews')
    customer = relationship('Customer', backref='reviews')

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

restaurant1 = Restaurant(name='Kwa Mathe', price=200)
restaurant2 = Restaurant(name='Kempinski', price=3000)

customer1 = Customer(first_name='Sam', last_name='Son')
customer2 = Customer(first_name='King', last_name='Kong')

review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

session.commit()

restaurants = session.query(Restaurant).all()
customers = session.query(Customer).all()
reviews = session.query(Review).all()

print("Restaurants:")
for restaurant in restaurants:
    print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

print("\nCustomers:")
for customer in customers:
    print(f"ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

print("\nReviews:")
for review in reviews:
    print(f"ID: {review.id}, Rating: {review.star_rating}, Restaurant ID: {review.restaurant_id}, Customer ID: {review.customer_id}")
