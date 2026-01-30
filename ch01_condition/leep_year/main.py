year = int(input('연도를 입력하여 주세요. >>> '))
result = False

if year < 0:
    print('값이 올바르지 않습니다.')
elif year%400 == 0 or (year%4 == 0 and year%100 != 0): #100의 배수가 아닌 4의 배수이거나 400의 배수 = 윤년
    print(f'{year}년은 윤년입니다.')
else:
    print(f'{year}년은 윤년이 아닙니다.')