from person import Person
import random

class Generator:
    
    people = []
    
    def __init__(self, people):
        self.people = people

    def print_data(self):
        for person in self.people:
            print(f"{person.get_full_name()} - {person.gift_giver.get_full_name()}")
            
    def reset(self):
        for person in self.people:
            person.set_gift_giver(None)
            person.set_gifted_person(None)
            
    def valid(self):
        for person in self.people:
            if not person.has_gift_giver():
                return False
        return True

    def get_gift_giver(self, person):
        gift_givers = self.people.copy()
        random.shuffle(gift_givers)
        for gift_giver in gift_givers:
            if gift_giver != person and not gift_giver.has_gifted_person():
                return gift_giver

    def generate(self):
        for person in self.people:
            gift_giver = self.get_gift_giver(person)
            if gift_giver:
                person.set_gift_giver(gift_giver)
                gift_giver.set_gifted_person(person)
        if not self.valid():
            self.reset()
            self.generate()

    def run(self):
        self.generate()
        self.print_data()