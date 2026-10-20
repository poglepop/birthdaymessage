from person import person

class people:
    def __init__(self):
        self.people = []

    def add_person(self, person: person):
        self.people.append(person)

    def remove_person(self, person: person):
        self.people.remove(person)
        
    def get_people(self):
        return self.people