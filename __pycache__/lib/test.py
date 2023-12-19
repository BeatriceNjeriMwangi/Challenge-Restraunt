from customer import Customer
from restraunt import Restaurant
from review import Review

customer1 = Customer("Beatrice", "njeri")
restaurant1 = Restaurant("Sonford")

review1 = customer1.add_review(restaurant1, 3)
# review2 = Review.add_review(customer1, restaurant1, 5)

# for review in Review.all():
#     # print(f"Review Rating: {review.get_rating()}, Customer Data: {review.customer.__dict__}, Restaurant Data: {review.restaurant.__dict__}")

# print(Review.all())
for customer in Customer.all():
    print ({customer.full_name() } )

for restaurant in Restaurant.all():
    print ({restaurant.name()})
