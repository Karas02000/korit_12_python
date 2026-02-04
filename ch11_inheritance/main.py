class Person:
    def __init__(self,name):
        self.name = name
    def eat(self, food):
        print(f'{self.name}은(는) {food}를 먹습니다.')
homer = Person('호머')
homer.eat('도넛')

class Student(Person):
    def __init__(self,name,school):
        super().__init__(name)
        self.school = school
    def study(self,school):
        print(f'{self.name}은(는) {school}에서 공부합니다.')
    def eat(self,food):
        print(f'{self.school}에서',end=" ")
        super().eat(food)

potter = Student('해리', '호그와트')
potter.eat('감자')