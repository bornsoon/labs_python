"""
자료형
"""
num1 = 1.23456
print(round(num1,2))

c = complex(1, 2)  # 복소수
print(c)

print(1==1)

print("="*10)

# String 형
str0 = "Hello Python!!!"
print(str0[0])  # indexing
print(str0[-1])
print(str0[0:5])  # slicing
print(str0[6:])
print(str0[:5])
print(str0[:])
print(str0[6:-1])
print(str0[::3])  # (start:end:step)
print(str0[::-1])
print(str0[4::-1])
print(str0[0:5:2])

str1 = '*'
str2 = '!'
print(str1+str2)
print(str1*10)

print("abcde".count("b"))
print("a:b:c:d".split(":"))
print("ababac".replace("a", "v"))
print(",".join("abc"))
print("11".zfill(5))

# row 문자열
str3 = r'\'Row\'\r\n문자열'    # 파일 경로 문자열에 많이 씀!!!
print(str3)

# 논리형
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(""))
print(bool("False"))
print(bool(None))

# None
x = ""                               # 유효한 값
y = None                             # 유효하지 않은 값의 표현
z = None

print(type(x), type(y))
print(id(x), id(y), id(z))

if x == "":
    print("x는 값이 없습니다.")

if not y:
    print("y는 값이 없습니다.")

def void_function():
    a = 10

result = void_function()
print(result)                         # 기본 반환값 None
print(type(void_function))