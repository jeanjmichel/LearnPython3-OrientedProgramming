import datetime
from datetime import timedelta

class Person:
    def __init__(self, person_id, person_name, person_gender, person_date_of_birth):
        self.person_id = person_id
        self.person_name = person_name
        self.person_gender = person_gender 
        self.person_date_of_birth = person_date_of_birth

    def __str__(self):
        return "class Person[person_id: {0} person_name: {1} person_gender: {2} person_date_of_birth: {3}]".format(self.person_id, self.person_name, self.person_gender, self.person_date_of_birth.strftime("%d/%m/%Y"))
    