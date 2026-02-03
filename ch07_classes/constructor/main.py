# class Candy:
#     def set_info(self,shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# satang = Candy()
# satang.set_info('구형','갈색')
# satang.show_info()
#
# class Candy2:
#     def __init__(self,shape,color):
#         self.shape = shape
#         self.color = color
#     def show_info(self):
#         print(f'사탕 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# satang2 = Candy2(shape='정육면체', color='흰색')
# satang2.show_info()
#
# class Sample:
#     def __init__(self):
#         print('인스턴스가 생성되었습니다.')
#     def __del__(self):
#         print('인스턴스가 소멸되었습니다.')
#
# smaple = Sample()
# print()
# del smaple
# print('객체 소멸 이후 작성한 코드입니다. 프로그램 종료 전에 이미 객체가 삭제되었음을 알 수 있습니다.')
#

class USB:
    def __init__(self,capacity):
        self.capacity = capacity
        print('USB 객체가 생성되었습니다.')
    def get_info(self):
        print(f'{self.capacity}GB USB')

usb = USB(64)
usb.get_info()

class Person:
    def __init__(self,name):
        self.name = name
        print(f'{name} is born.')
    def __del__(self):
        print(f'{self.name} is dead.')

man = Person('James')
woman = Person('Emily')

del man
print('man객체 소멸')