for i in range(10):
    print(i+1)
'''
range 사용시 주의점
1. 기본적으로 시작값은 0
2. 종료값은 미만의 개념으로 세기에 10으로 작성시 9까지만 리턴된다.

range(시작값, 한계값, 증감값)
시작값 : 생략 가능, 생략시 0부터 시작
한계값 : 생략시 무한히 진행.
증감값 : 생략 가능, 생략시 1로 적용.
'''
for i in range(11):
    print(i)
for i in range(3,11):
    print(i)
for i in range(3,11,2):
    print(i)
print()
print(i)

nums = range(1,11)
if 5 in nums:
    print('5가 nums list 내에 있습니다.')
else:
    print('5가 nums list 내에 없습니다.')

print(5 in nums)