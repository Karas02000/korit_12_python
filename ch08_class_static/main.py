# class Korean:
#     contry = '한국'
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# korean = Korean('김일',21,'서울특별시 마포구')
# print(korean.name)
# print(korean.contry)
# print(Korean.contry)
#
# class Korean2:
#     contry = '대한민국'
#
#     @classmethod
#     def trip(cls, travelling_site):
#         if cls.contry == travelling_site:
#             print('국내 여행입니다.')
#         else:
#             print('해외 여행입니다.')
#
# Korean2.trip('대한민국')
# Korean2.trip('미국')
#
# person2 = Korean2()
# person2.trip('일본')
#
# class Korean3:
#     contry = '한국'
#
#     @staticmethod
#     def slogan():
#         print('Imagine Your Korea! 📌')
#     @staticmethod
#     def slogan2(str_example):
#         print(f'Imagine Your Korea! 📌 {str_example}')
#
# Korean3.slogan()
# Korean3.slogan2('근데 너무 춥다.')
#
# class Bag:
#     cnt = 0
#     def __init__(self):
#         Bag.cnt += 1
#
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.cnt-=1
#     @classmethod
#     def remain_bag(cls):
#         return cls.cnt
# print(Bag.cnt)
# bag1 = Bag()
# print(Bag.cnt)
# bag2 = Bag()
# print(Bag.cnt)
# bag3 = Bag()
# print(Bag.cnt)
# bag4 = Bag()
# print(Bag.cnt)
# bag5 = Bag()
# print(Bag.cnt)
# bag3.sell()
# print(Bag.cnt)
# bag4.sell()
# print(Bag.cnt)
#
# print(f'현재 가방 재고 : {Bag.cnt}')
# bag1.sell()
# print(f'현재 가방 재고 : {Bag.cnt}')


class Person:
    popultion = 0

    def __init__(self, name):
        self.name = name
        print(f'{name}이(가) 태어났습니다.')
        Person.popultion += 1
    def __del__(self):
        Person.popultion -= 1
        print(f'RIP {self.name}')
    @classmethod
    def get_population(cls):
        return cls.popultion
man = Person('김일')
woman = Person('김이')

print(f'전체 인구수 : {Person.get_population()}')

del man
print(f'전체 인구수 : {Person.get_population()}')