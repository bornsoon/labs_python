def fn():
    """
    
    :param 없음
    :return 없음
    """

help(fn)
print(fn.__doc__)

'''
변수, 상수, 리터럴
'''
import sys

# 다중 할당문
a, b, c = 1, [2, 3], 4
print(a, b, c)
print(b[0])

'''
Python은 기본형이 없음!!!!!!! (주소만 넘어감)
         참조형만 있음!!!!!!!
'''

a = 10  # 10의 주소가 a로
b = None
print(a, id(a), b, id(b))

b = a   # 10의 주소가 b로
print(a, id(a), b, id(b))

a = 20  # 20의 주소가 a로
print(a, id(a), b, id(b))

# 상수
PI = 3.1415
PI = 3.14 # 변경됨

def CONST_PI():
    return 3.1415

print(5*CONST_PI())

'''
자료형
'''
# 숫자형
a = 123
a = sys.maxsize
b = sys.maxsize + 200

print(f'{a}, {b}') # 오버플로우가 발생 안함!!!!
a = 3.14
print(f'{a}, {b}')

# 문자형
a = 'a'

# 논리형
a = True
print(f'{a}')

# Type Hint
# 파이썬 버전 3.5 부터 가능
a: str = 'abcde'
b: int = 1
c: float = 2.5
d: list = [1, 2, 3]
e: int   # 나중에 초기화. 초기화 안하면 오류
e = 1.2

print(f'{a}, {b}, {c}, {d}, {e}')

# Generic Type: Wrapper Class 이용
from typing import List, Dict, Tuple, Set, Optional

a: List[int] = [1, 3, 5]
b: Dict[int, str] = {1:'a', 2:'b'}
c: Tuple[str, int, float] = ('abc', 1, 0.9)
d: Set[int] = []
e: Optional[int]

print(f'{a}, {b}, {c}, {d}, {e}')

def add(a: int, b: int) -> int:
    return a+b

print(add(1, 1.2))