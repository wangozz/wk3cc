# wk3cc/main.py

from restaurant.restaurant import Restaurant
from customer.customer import Customer
from review.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database connection
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Example usage:

# Creating a new restaurant
new_restaurant = Restaurant(name='New Restaurant', price=3)
session.add(new_restaurant)

# Creating a new customer
new_customer = Customer(first_name='John', last_name='Doe')
session.add(new_customer)

# Adding a review
new_review = Review(star_rating=4, restaurant=new_restaurant, customer=new_customer)
session.add(new_review)

# Committing changes to the database
session.commit()

# Fetching data
restaurants = session.query(Restaurant).all()
customers = session.query(Customer).all()
reviews = session.query(Review).all()

# Printing data
print("Restaurants:")
for restaurant in restaurants:
    print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

print("\nCustomers:")
for customer in customers:
    print(f"ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

print("\nReviews:")
for review in reviews:
    print(f"ID: {review.id}, Rating: {review.star_rating}, Restaurant ID: {review.restaurant_id}, Customer ID: {review.customer_id}")
