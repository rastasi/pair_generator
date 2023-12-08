class Person:
    first_name = ""
    last_name = ""
    sex = ""
    gift_giver = None
    gifted_person = None
    
    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        
    def is_male(self):
        return self.sex == "male"
    
    def is_female(self):
        return self.sex == "female"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def set_gift_giver(self, person):
        self.gift_giver = person

    def has_gift_giver(self):
        return self.gift_giver != None
    
    def set_gifted_person(self, person):
        self.gifted_person = person
        
    def has_gifted_person(self):
        return self.gifted_person != None
