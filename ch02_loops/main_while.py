'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 조건문이 거짓이 될 때까지 이하의 실행문이 반복된다.

초기화
while 조건문1:
    실행문1
    증감문

'''
n1=1
while n1<=10:
    print(n1,end=' / ')
    n1+=1

print()

n2=10
while n2>0:
    print(n2,end=' / ')
    n2-=1


dan = 2
while dan<10:
    number = 1
    while number < 10:
        print(f'{dan} × {number} = {dan * number}')
        number+=1
    dan+=1
    print()