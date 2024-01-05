from review import Review

class Customer:
    all_list = []

    def __init__(self, name, f_name):
        self.name = name
        self.f_name = f_name
        self.all_list.append(self)

    @property
    def given_name(self):
        return self._name

    @given_name.setter
    def given_name(self, name):
        self._name= name

    def family_name(self):
        return self.f_name
    
    @family_name.setter
    def family_name(self, f_name):
        self._f_name= f_name

    @property
    def full_name(self):
        return f"{self._name} {self._f_name}"

    @classmethod
    def all(cls):
        return cls.all_list

    def restaurants(self):
        return list({review.restaurant for review in Review.all() if review.customer == self})

    def add_review(self, restaurant, rating):
        new_review = Review(rating, self, restaurant)
        return new_review

    def num_reviews(self):
        count = 0
        for review in Review.all():
            if review.customer() == self:
                count += 1
        return count
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_list:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_list if customer.given_name() == name]