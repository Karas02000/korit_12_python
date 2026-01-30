# eng_name = input('당신의 이름을 영어로 입력하세요.')
# eng_name_low = eng_name.lower()
# eng_name_up = eng_name.upper()
# print(f'{eng_name_low} / {eng_name_up}')


# def multiply(dan):
#     for n in range(1, 10):
#         print(f'{dan} × {n} = {dan*n}')
#
# multiply(int(input('몇 단을 출력하시겠습니까 >>> ')))

def vending_machine(n):
    money = n
    drink = 700
    buy = 0;

    print(f'음료수 = {buy}, 잔돈 = {money}원')
    while money > drink:
        buy+=1
        money-=drink
        print(f'음료수 = {buy}, 잔돈 = {money}원')

vending_machine(3000)