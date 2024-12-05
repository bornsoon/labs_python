"""
set
 - 가변형
 - dict의 키들로 구성
 - 기본적인 특징은 dict의 키와 같다
"""

a = {}
b = {1, 2, 3}
c = {1, 2, 3, 'a'}
d = set('hello world')
print(d)

# print(b[0])
e = list(b)
print(e[0])

# 집합연산자
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합
print(a ^ b)  # 여집합
print(a >= {1, 2})  # 부분집합