from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.restaurant import Restaurant
from customer.customer import Customer
from review.review import Review

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()


restaurant1 = Restaurant(name='Restaurant A', price=2)
restaurant2 = Restaurant(name='Restaurant B', price=3)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()

session.close()
