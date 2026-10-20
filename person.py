import datetime

class person:

    def __init__(self, name: str, surname: str, dob: datetime, relationship: str, importance: int):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.relationship = relationship
        self.importance = importance

    def edit_person(self, name: str, surname: str, dob: datetime, relationship: str, importance: int):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.relationship = relationship
        self.importance = importance

    def isBirthday(self) -> bool:
        if self.dob.year == datetime.datetime.now().year and self.dob.month == datetime.datetime.now().month and self.dob.day == datetime.datetime.now().day:
            return True
        else:   
            return False

    def isBirthdayMonth(self) -> bool:
        if self.dob.year == datetime.datetime.now().year and self.dob.month == datetime.datetime.now().month:
            return True
        else:   
            return False    