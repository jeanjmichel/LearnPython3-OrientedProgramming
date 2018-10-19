# _____       _               _ _                       
#|_   _|     | |             (_) |                      
#  | |  _ __ | |__   ___ _ __ _| |_ __ _ _ __   ___ ___ 
#  | | | '_ \| '_ \ / _ \ '__| | __/ _` | '_ \ / __/ _ \
# _| |_| | | | | | |  __/ |  | | || (_| | | | | (_|  __/
#|_____|_| |_|_| |_|\___|_|  |_|\__\__,_|_| |_|\___\___|
from student import Student
import datetime
from datetime import timedelta

class Main:
    semester_grade = []
    semester_grade.append("Algorithms")
    semester_grade.append("Programming Language I")
    semester_grade.append("Data Structure")
    semester_grade.append("Discrete Mathematics")

    student = Student(1, "Jean J. Michel", "M", datetime.date(1982, 2, 27), 201301322742, semester_grade)
    print(student)