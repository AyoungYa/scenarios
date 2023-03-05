from faker import Faker

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def getAge(self):
        return self.age

fake = Faker()

people = [Person(fake.name(), fake.random_int(min=1, max=100), fake.email()) for _ in range(5)]

# Sort people by age
people.sort(key=lambda person: person.getAge())

# Print sorted people
for person in people:
    print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}")
