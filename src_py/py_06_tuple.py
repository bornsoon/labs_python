"""
Tuple((~))

 - 불변형
 - 인덱스 이용(시퀀스) -> 순서가 있다.
 - 다양한 데이터 타입의 원소를 가질 수 있다.
"""

a = ()
b = (1, 2, 3)
c = (1, 2, 3, ('a', 'b', 'c'))

d = c[3][0]
print(d)

# b[1] = 5

# 인덱싱, 슬라이싱
a = (1, 2, 3, ['a', 'b', 'c'])
print(a[0])
print(a[-1], a[3])
print(a[3][0])
print(a[3][:2])

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[0])  # indexing
print(a[:5])

# 연산자
print((1, 2, 3) + (3, 4, 5))
print((1, 2) * 3)

# 함수
print(len(a), min(a), max(a), sum(a))
print(sorted(a))   # 리스트로 반환

# tuple 컴프리헨션
list = tuple(n for n in range(1, 100))
print(list)

list = tuple(n*2 for n in range(1, 100))
print(list)

list = tuple(n for n in range(1, 100) if n%2==0)
print(list)