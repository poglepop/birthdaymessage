import datetime

from people import people
from person import person

class process_birthdays:

    def __init__(self, check_date: datetime):
        self.check_date = check_date

    def check_birthdays(self, people: people): 
        birthday_people = []
        for person in people.get_people():
            if person.isBirthdayMonth():
                birthday_people.append(person)
        return birthday_people

    def generate_message(self, person: person) -> str:
        return f"Happy Birthday {person.name} ! Wishing you a wonderful day filled with love and joy."

    def send_message(self, person: person):
        message = self.generate_message(person)
        print(message)
    




