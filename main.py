
import datetime

from people import people 
from person import person
from birthdays import process_birthdays

def main():
    # Create a people object
    my_people = people()

    # Create some person objects
    person1 = person("John", "Doe", datetime.datetime(1990, 5, 15), "Friend", 5)
    person2 = person("Jane", "Smith", datetime.datetime(1985, 8, 20), "Family", 10)
    person3 = person("Alice", "Johnson", datetime.datetime(2026, 10, 20), "Colleague", 3)
    person4 = person("Neville", "Clarkson", datetime.datetime(2026, 10, 25), "Colleague", 3)

    print(person1.name, person1.surname, person1.dob, person1.relationship, person1.importance)

    # Add the person objects to the people object
    my_people.add_person(person1)
    my_people.add_person(person2)
    my_people.add_person(person3)
    my_people.add_person(person4)

    print(my_people.get_people())

    # Create a process_birthdays object with the current date
    birthday_processor = process_birthdays(datetime.datetime.now())

    # Check for birthdays in the current month
    birthday_people = birthday_processor.check_birthdays(my_people)
    print(birthday_people)

    # Send birthday messages to those who have birthdays this month
    for birthday_person in birthday_people:
        birthday_processor.send_message(birthday_person)

main()