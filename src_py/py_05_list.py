"""
collection(자료구조)
 - List, Tuple, Dictionary, Set
"""

# Range
r = range(5) # (stop | start, stop | start, stop, step)
for i in r:
    print(i)

# 패킹(packing), 언패킹(unpacking)
a, b, c, d, e = '안녕하세요'  # 언패킹
print(a, b, c, d, e)

f = a, e  # 패킹
print(f)

g, h = f
print(g, h)

s, *m, e = '안녕하세요'

'''
List
 - 가변형
 - 인덱스 이용(시퀀스) -> 순서가 있다.
 - 다양한 데이터 타입의 원소를 가질 수 있다.
'''
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1], a[3])
print(a[3][0])
print(a[3][:2])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0])  # indexing
print(a[:5])

a[0] = 10
print(a)

a[1:4] = [32, 33, 34]
print(a)

# 연산자
print([1, 2, 3] + [3, 4, 5])
print([1, 2] * 3)

# 함수
print(len(a), min(a), max(a), sum(a))
print(sorted(a))

# 메소드
a.append(6)
b = a.copy()
b.clear()

# List 컴프리헨션
list = [n for n in range(1, 100)]
print(list)

list = [n*2 for n in range(1, 100)]
print(list)

list = [n for n in range(1, 100) if n%2==0]
print(list)