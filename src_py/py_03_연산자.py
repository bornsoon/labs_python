"""
연산자
"""

c = 0.1 + 0.1 + 0.1 - 0.3
print(c)                               # 5.551115123125783e-17


# 실수가 나오면 오차 주의!!
# 실수를 분수(정수)로 바꿔어주는 decimal 모듈!!!
import decimal

print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))

# decimal 모듈은 사용자가 변경할 수 있는 정밀도(기본값은 28자리)를 가지며, 주어진 문제에 따라 필요한 만큼 커질 수 있다.
print(decimal.Decimal('0.11') + decimal.Decimal('0.11') + decimal.Decimal('0.11') - decimal.Decimal('0.3192111'))

a = 10; b = 11; b += a; print(b)

# 논리 연산자
a = True; b = False
print(a and b)
print(a or b)
print(not(a))

# 삼항 연산자
a = 3
print("짝수" if a%2==0 else "홀수")