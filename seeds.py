from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.restaurant import Restaurant
from customer.customer import Customer
from review.review import Review

# Set up the database connection
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define sample data

# Restaurants
restaurant1 = Restaurant(name='Restaurant A', price=2)
restaurant2 = Restaurant(name='Restaurant B', price=3)

# Customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

# Reviews
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

# Add sample data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()

# Close the session
session.close()
