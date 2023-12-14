from person import Person
from generator import Generator
from person_printer import PersonPrinter
import random

people = [
    Person(first_name="Dora", last_name="Pekk-Juhasz", sex="female"),
    Person(first_name="Zsolt", last_name="Tasnadi", sex="male"),
    Person(first_name="Balazs", last_name="Bellanyi", sex="male"),
    Person(first_name="Blanka", last_name="Szigethy", sex="female"),
]

# Generator(people).run()

p = PersonPrinter(people)
p.run()