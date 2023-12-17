class   Customer:
    all=[]
    def __init__(self, name, f_name):
        self.name = name
        self.f_name = f_name
        full_name = f"{name} {f_name}"
        self.add_customer_to_all(full_name)
    
    def given_name(self):
        return self.name
    def family_name(self):
        return self.f_name
    def full_name(self):
        return (f"{self.name} {self.f_name}")
    
    @classmethod
    def add_customer_to_all(cls, full_name):
        cls.all.append(full_name)
    @classmethod
    def show_customer(cls):
        print(cls.all)
        pass
beatrice = Customer("beatrice", "njeri")
beatrice.full_name()
Customer.show_customer()




