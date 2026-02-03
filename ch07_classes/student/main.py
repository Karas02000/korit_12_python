class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self._grades = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

student1 = Student('김일', 2026001)
print(f'학생 이름 : {student1.name}')

student1.name = '김영'

print(f'변경된 학생 이름 : {student1.name}')
print(student1._name)