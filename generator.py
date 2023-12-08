from person import Person
import random

class Generator:
    
    def __init__(self, people):
        self.people = people

    def print_data(self):
        i = 0
        while i < len(self.people):
            person = self.people[i]
            print(f"{person.get_full_name()} - {person.gift_giver.get_full_name()}")
            i = i + 1
            
    def reset(self):
        i = 0
        while i < len(self.people):
            person = self.people[i]
            person.set_gift_giver(None)
            person.set_gifted_person(None)
            i = i + 1
            
    def valid(self):
        i = 0
        while i < len(self.people):
            person = self.people[i]
            if not person.has_gift_giver():
                return False
            i = i + 1
        return True

    def get_gift_giver(self, person):
        gift_givers = self.people.copy()
        random.shuffle(gift_givers)
        i = 0
        while i < len(gift_givers):
            gift_giver = gift_givers[i]
            if gift_giver != person and not gift_giver.has_gifted_person():
                return gift_giver
            i = i + 1

    def generate(self):
        i = 0
        while i < len(self.people):
            person = self.people[i]
            gift_giver = self.get_gift_giver(person)
            if gift_giver:
                person.set_gift_giver(gift_giver)
                gift_giver.set_gifted_person(person)
            i = i + 1
        if not self.valid():
            self.reset()
            self.generate()

    def run(self):
        self.generate()
        self.print_data()