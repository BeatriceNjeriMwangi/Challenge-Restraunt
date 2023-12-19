# restaurant.py
class Restaurant:
    new_rest = []

    def __init__(self, name):
        self._name = name
        self.reviews_list = []
        self.new_rest.append(self)

    def name(self):
        return self._name

    def add_review(self, review):
        self.reviews_list.append(review)

    def reviews(self):
        return self.reviews_list

    @classmethod
    def all(cls):
        return cls.new_rest

    def customers(self):
        return list({review.customer() for review in self.reviews_list})

    def average_star_rating(self):
        if not self.reviews_list:
            return 0
        total_star_rating = sum([review.rating for review in self.reviews_list])
        return total_star_rating / len(self.reviews_list)
