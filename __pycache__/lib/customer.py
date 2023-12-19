from review import Review

class Customer:
    all_list=[]
    def __init__(self, name, f_name):
        self.name = name
        self.f_name = f_name
       
        self.all_list.append(self)
        
    
    def given_name(self):
        return self.name
    def family_name(self):
        return self.f_name
    def full_name(self):
        return f"{self.name} {self.f_name}"
    
    @classmethod
    def all(cls):
        return cls.all_list
    
    def restaurants(self):
        return list({review.restaurant for review in Review.all()if review.customer==self})

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        # self.reviews.add(new_review)
        return new_review
        pass





