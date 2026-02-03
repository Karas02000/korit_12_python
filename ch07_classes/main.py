class Person:
    def set_info(self,name,age,tel,adress):
        self.name = name
        self.age = age
        self.tel = tel
        self.adress = adress

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'이름 : {self.age}')
        print(f'이름 : {self.tel}')
        print(f'이름 : {self.adress}')

    def show_info2(self):
        return f'제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}인데, {self.adress}에 살고있습니다.'

person1 = Person()
person1.set_info(age=20, tel='010-1234-5678',adress='부산광역시 부산진구',name='김일')
person1.show_info()
print(person1.show_info2())

