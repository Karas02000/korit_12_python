# class Person:
#     def __init__(self,name):
#         self.name = name
#     def eat(self, food):
#         print(f'{self.name}은(는) {food}를 먹습니다.')
# homer = Person('호머')
# homer.eat('도넛')
#
# class Student(Person):
#     def __init__(self,name,school):
#         super().__init__(name)
#         self.school = school
#     def study(self,school):
#         print(f'{self.name}은(는) {school}에서 공부합니다.')
#     def eat(self,food):
#         print(f'{self.school}에서',end=" ")
#         super().eat(food)
#
# potter = Student('해리', '호그와트')
# potter.eat('감자')

# class Car:
#     max_oil = 50
#     def __init__(self, oil):
#         self.oil = oil
#     def add_oil(self, oil):
#         print(f'기름을 {(oil+(Car.max_oil-oil))-self.oil} 주유 했습니다.')
#         if oil <= 0:
#             return
#         self.oil += oil
#         if self.oil > Car.max_oil:
#             self.oil = Car.max_oil
#     def car_info(self):
#         print(f'현재 주유 상태: {self.oil}')
#
# class Hybrid(Car):
#     max_battery = 30
#     def __init__(self, oil, amount):
#         super().__init__(oil)
#         self.amount = amount
#         print('하이브리드 차량이 생산되었습니다.')
#     def charge(self, amount):
#         print(f'전기를 {(amount + (Hybrid.max_battery - amount)) - self.amount} 충전 했습니다.')
#         if amount <= 0:
#             return
#         self.amount += amount
#         if self.amount > Hybrid.max_battery:
#             self.amount = Hybrid.max_battery
#     def hybrid_info(self):
#         super().car_info()
#         print(f'현재 충전 상태: {self.amount}')
#
# car = Hybrid(oil= 0, amount= 0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info()
'''
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의하여 self.name을 출력하시오(call1() 유형)
2. Shape 클래스를 상속 받는 서브 클래스 Circle을 정의하시오.
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자에서 radius도 추가할 것.
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것. -> call3()
        (넓이 = 3.14 * radius * radius)
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의하시오.
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가집니다.
    - 생성자에서 width / height를 초기화할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것 -> call3()
        (넓이 = 너비 * 높이)
3. Circle과 Rectangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력할 것.


circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다.
이름이 원1인 원의 넓이는 ____ 입니다.
원의 넓이 : ____
너비가 10, 높이가 8인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
'''
import math


class Shape:
    def __init__(self, name):
        self.name = name
    def draw(self):
        print(self.name)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {radius}인 {name}이(가) 생성되었습니다.')
    def area(self):
        return self.radius * self.radius * 3.14
    def draw(self):
        print(f'이름이 {self.name}인 원의 넓이는 {self.radius * self.radius * 3.14} 입니다.')

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가 {self.width}, 높이가 {self.height}인 {self.name}이(가) 생성되었습니다.')
    def area(self):
        return self.width * self.height
    def draw(self):
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.height * self.width} 입니다.')

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')