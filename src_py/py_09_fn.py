"""
Function Basic
"""
def helloworld(i):
    for n in range(i):
        print(f'{n}. Hello World!!!')

helloworld(5)

fn1 = helloworld
fn1(2)


########################

def sum1(a, opt):
    total = 0
    for n in a:
        total += opt(n)
    print(total)
    
def square(x):
    return x**2

########################


sum1(range(1, 11), square)
print(sum([n**2 for n in range(1, 11)]))

# 매개변수
p1 = [1, 2]
p2 = (1, 2)

def param(p):
    _p = p  # p.copy()
    _p[0] = 5
    print(_p)

param(p1)
print(p1)

# param(p2)
# print(p2)

def display_money(a, b='원'):
    print(f'{a}{b}')

display_money(1000, '원')
display_money(1000, '달러')
display_money(1000)

# 명명된 매개변수
display_money(b='달러', a=1000)

def param1(a):
    print(a[0], a[1], a[2])

param1([1, 2, 3])


# 언패킹
########################

def param2(a, b, c):
    print(a, b, c)

param2(*[4, 5, 6])

lst = [4, 6, 7] 
param2(*lst)

########################


# 패킹
########################

def param3(*args):  # 패킹
    print(args[0], args[1], args[2])

param3(1, 2, 3)
# 오류 param3([1, 2, 3])
param3(*[1, 2, 3])
# 오류 param3(1, 2)
param3(1, 2, 3, 4)

########################


# 딕셔너리의 언패킹 ( **{} )
################################################

def param4(a, b, c):
    print(a, b, c)

param4(**{'a': 1, 'b': 2, 'c': 3})  # 언패킹

################################################


# 딕셔너리의 패킹 ( **args )
################################################

def param5(**args):   # 패킹
    print(args['a'], args['b'], args['c'])

param5(a=11, b=22, c=33)
param5(**{'a': 11, 'b': 12, 'c': 13})

################################################


# 매개변수의 언패킹 ( args1, *args, **args )
################################################

def param6(a, *b, **c):  # 순서 중요
    for i in b:
        print('{} ({}{})'.format(a*i, i, c['단위']))

param6('*', 3, 5, 14, 8, 30, 29, 단위='대')
param6('#', *{3, 5, 14, 8, 30, 29}, **{'단위':'대'})

################################################


# lambda
################################################

plus= lambda a,b: a+b
print(plus(1, 2))

def calc(a, b, fn):
    fn(a/b)
calc(1, 2, lambda a: print(a))

def calc(a, b, fn):
    fn(a/b)
calc(1, 2, lambda a: print(a))
calc(1, 2, lambda a: print('{:10.2f}'.format(a)))