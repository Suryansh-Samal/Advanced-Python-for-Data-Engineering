class School:

    def __init__(self, school_name):
        self.school_name = school_name

    def school_info(self):
        return f'{self.school_name}'

class Standard (School):

    def __init__(self, std, school_name):
        self.std = std
        School.__init__(self, school_name)

    def standard_info(self):
        response = School.school_info(self)
        return f'Standard: {self.std}\nSchool: {response}'

class Student (Standard):

    def __init__(self,student_name:str, std, school_name:str):
        self.student_name= student_name
        Standard.__init__(self,std, school_name)

    def complete_info(self):
        response = Student.standard_info(self)
        print(f'Student: {self.student_name}\n{response}')

student1 = Student('Suryansh', 'X', "Holy Angel's")
student1.complete_info()