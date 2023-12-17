from customer import Customer
from restraunt import Restaurant

class Review:
    all_reviews = []

    def __init__(self, rating, customer, restaurant):
        self.rating = rating
        self.customer = customer
        self.restaurant = restaurant

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    @classmethod
    def create_review(cls, customer, restaurant, rating):
        new_review = cls(rating, customer, restaurant)
        cls.all_reviews.append(new_review)
        return new_review

customer1 = Customer("Beatrice", "njeri")
restaurant1 = Restaurant("Sonford")

review1 = Review.create_review(customer1, restaurant1, 3)
review2 = Review.create_review(customer1, restaurant1, 5)

for review in Review.all():
    print(f"Review Rating: {review.get_rating()}, Customer Data: {review.customer.__dict__}, Restaurant Data: {review.restaurant.__dict__}")

print(Review.all())
