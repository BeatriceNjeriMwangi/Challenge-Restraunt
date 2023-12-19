from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("Beatrice", "njeri")
customer2 = Customer("Dan", "Mwangi")
restaurant1 = Restaurant("Sonford")

review1 = customer1.add_review(restaurant1, 3)

review2 = customer2.add_review(restaurant1, 5)

for customer in Customer.all():
    print(f"{customer.full_name()} Number of reviews: {customer.num_reviews()}")

for restaurant in Restaurant.all():
    print(f"{restaurant.name()}  {restaurant.average_star_rating()}")