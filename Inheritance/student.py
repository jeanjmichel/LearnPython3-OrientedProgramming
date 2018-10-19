from person import Person

class Student(Person):
    def __init__(self, person_id, person_name, person_gender, person_date_of_birth, student_enrollment, student_semester_grade):
        self.person_id = person_id
        self.person_name = person_name
        self.person_gender = person_gender
        self.person_date_of_birth = person_date_of_birth
        self.student_enrollment = student_enrollment
        self.student_semester_grade = student_semester_grade
        
    def __str__(self):
        return "class Student[person_id: {0} person_name: {1} person_gender: {2} person_date_of_birth: {3} student_enrollment: {4} student_semester_grade: [{5}]".format(self.person_id, self.person_name, self.person_gender, self.person_date_of_birth.strftime("%d/%m/%Y"), self.student_enrollment, self.student_semester_grade)