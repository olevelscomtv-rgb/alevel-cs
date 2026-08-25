class Student:
    def __init__(self, student_id, student_name, age, marks):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__age = age
        self.__marks = 0

    def add_info(self, id, name, new_age, new_marks):
        id = int(input("Please enter your ID: "))
        name = input("Please enter your NAME: ")
        new_age = int(input("Please enter your AGE: "))
        new_marks = int(input("Please enter your MARKS: "))
        self.__student_id = id
        self.__student_name = name
        self.__age = new_age
        self.__marks = new_marks

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_marks(self):
        return self.__marks

    def grades(self):
        if self.__marks >= 90 and self.__marks <= 100:
            grade = "A"
            return grade
        elif self.__marks >= 80 and self.__marks < 90:
            grade = "B"
            return grade
        elif self.__marks >= 70 and self.__marks < 80:
            grade = "C"
            return grade
        elif self.__marks >= 60 and self.__marks < 70:
            grade = "D"
            return grade
        else:
               grade = "F"
               return grade

    def pass_or_no(self):
        if self.grades() != "F":
            return "Pass"
        else:
            return "Fail"

    def update_marks(self, uptd_marks):
        self.__marks = uptd_marks
        return f"Your new marks are {uptd_marks}"

