"""
제어문
"""

a = 3

if a % 2 == 0:
    print('짝수')
else:
    print('홀수')

c = '짝수' if a % 2 == 0 else '홀수'
print(c)

(a % 2 == 0) and print('짝수')
(a % 2 == 0) or print('홀수')
print(print('짝수'))

a, b = 6, 0

if b and a % b == 0:
    print(f'{a}는 {b}의 배수입니다.')
else:
    print('0입니다.')

# 요일출력
import datetime

d = datetime.datetime.today().weekday()

# 오늘의 요일을 한글로 출력하세요. (월0,화1~)
if d==0:
    print('월')
elif d==1:
    print('화')

e = '월화수목금토일'
print(e[d])

a = 0
while a < 10:
    a += 1
    print(f'{str(a)*a}')

for a in range(1, 11):
    print(f'{str(a)*a}')

a = [('사과', 1000, 2), ('배', 2000, 1), ('멜론', 3000, 2)]
total = 0
for (b, c, d) in a:
    total += c*d
    print(f'{b}({d}) {c*d}원')
else:                       ## else문은 for문이 끝나야지만 실행이 된다!!!!
    print(f'총합: {total}원')