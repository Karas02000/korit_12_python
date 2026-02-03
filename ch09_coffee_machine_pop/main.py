MENU = {
    '에스프레소' : {
        '재료' : {
            '물' : 50,
            '커피' : 18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
        '재료' : {
            '물' : 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료' : {
            '물' : 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격' : 3.0,
    },
}

resorces = {
    '물' : 300,
    '우유' : 200,
    '커피' : 100,
}
# resorces = {
#     '물' : 0,
#     '우유' : 0,
#     '커피' : 0,
# }
profit = 0

# for key in MENU['에스프레소']['재료']:
#     resorces[key] -= MENU['에스프레소']['재료'][key]*2
#
# print(resorces)

# coffee = '라떼'
# order = 1
# for key in MENU[coffee]['재료']:
#     resorces[key] -= MENU[coffee]['재료'][key] * order
# profit += MENU[coffee]['가격'] * order
#
# print(resorces)
# print(profit)

def report():
    print(f'물: {resorces['물']}ml')
    print(f'우유: {resorces['우유']}ml')
    print(f'커피: {resorces['커피']}g')
    print(f'돈: ${profit}')

def is_resorce_enough(order_ingredients):
    enough = True
    for key in order_ingredients:
        if resorces[key] < order_ingredients[key]:
            print(f'죄송합니다. {key}이(가) 부족합니다.')
            enough = False
    if enough:
        return True
    else:
        return False

def process_coins():
    coins = {
        'quaters':0.25,
        'dimes':0.10,
        'nickles':0.05,
        'pennies':0.01,
    }
    total = 0.0
    for coin in coins:
        total += int(input(f"{coin} >>> "))*coins[coin]
    return round(total,2)

def is_transaction_successful(money_received ,drink_cost):
    global profit
    change = 0
    if money_received >= drink_cost:
        profit += drink_cost
        change = money_received - drink_cost
        if change > 0:
            print(f'거스름돈 ${round(change,2)}를 반환합니다.')
        return True
    else:
        print("돈이 부족합니다. 돈을 반환합니다.")
        return False

def make_coffee(choice ,order_ingredients):
    print(f'{choice}이(가) 나왔습니다.')
    for key in order_ingredients:
        resorces[key] -= order_ingredients[key]

is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>> ')
    if choice == 'off':
        print('자판기가 종료되었습니다.')
        break
    elif choice == 'report':
        report()
    elif choice in ['에스프레소','라떼','카푸치노']:
        drink = MENU[choice]
        if is_resorce_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received,drink['가격']):
                make_coffee(choice, drink['재료'])
    else:
        print('잘못 입력하셨습니다.')