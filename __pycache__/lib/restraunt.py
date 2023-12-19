

class Restaurant:
    new_rest = []

    def __init__(self, name):
        self._name = name
        self.reviews_list=[]
        self.new_rest.append(self)

    def name(self):
        # if type(self.name) ==str:
            return self._name
        
       
    def add_review(self, review):
        self.reviews.append(review)

    def reviews(self):
        return self.reviews_list
    
    @classmethod
    def all(cls):
        return cls.new_rest
    
    def customers(self):
        return list({review.customer() for review in self.reviews_list})
    pass
