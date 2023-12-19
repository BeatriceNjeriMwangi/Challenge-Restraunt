class Review:
    all_reviews = []

    def __init__(self, rating, customer, restaurant):
        self.rating = rating
        self._customer_obj = customer
        self._restaurant_obj = restaurant
        self.all_reviews.append(self)
        restaurant.reviews_list.append(self)

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer_obj

    def restaurant(self):
        return self._restaurant_obj