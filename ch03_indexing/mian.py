str_example = 'Hello World!'


for num in range(len(str_example)):
    print(str_example[num],end='')
print()
for str in str_example:
    print(str, end='')

'''
마이너스 인덱스 : 뒤에서 세는 인덱스. 시작값은 -1

슬라이싱 : 배열에서 특정 값들을 규칙적으로 빼서 리턴하기 위한 기능 
형식 : 변수명[시작 인덱스 : 종료 인덱스 : 증감값]
기본적인 특징들 range의 그것과 같다.
다만 함수인 range와 달리 슬라이싱은 함수가 아니기에 ,가 아닌 :로 값을 구분한다.
'''
print()
print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])
print(str_example[-7])

number=input('네 자리 숫자를 입력하세요 >>> ')
print(f'맨 마지막 숫자는 {number[-1]}입니다.')

if int(number[-1])%2==0 :
    result = '짝수'
else:
    result = '홀수'
print(f'맨 마지막 숫자는 {number[-1]}이며, {result}입니다.')
'''
python 삼항 연산자
if-else 구조를 한줄로 줄여서 쓴다.
'''

result2 = '짝수'if int(number[-1])%2==0 else '홀수'

print(f'맨 마지막 숫자는 {number[-1]}이며, {result2}입니다.')