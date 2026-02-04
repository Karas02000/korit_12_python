from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? {menu.get_items()} >>> ')
    if choice == '정지':
        is_on = False
        print('자판기가 종료되었습니다.')
    elif choice == '정산':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice) is not None:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
