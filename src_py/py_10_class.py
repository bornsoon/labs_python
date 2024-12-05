"""
Class
"""
class Calc():
    def __init__(self):  # 생성자(self -> this)
        self._a = 0
        self._b = 0

    def add(self):
        return self._a + self._b
    
    def multi(self):
        return self._a * self._b
    
    def display(self):
        print(id(self), type(self), self._a, self._b)

calc = Calc()   # __init__ 이 호출됨
calc._a = 1
calc._b = 2
print(calc.add())
print(calc.multi())
calc.display()


###################################################################
# 파이썬 데이터 처리할 때는 pickle을 이용하자!!!!!!
###################################################################
import pickle
score = {'성명':'학생1', '국어':10, '영어':20, '수학':30}
print(pickle.dumps(score))  # 파이썬 pickle 객체로 정보 저장하기!!!

with open('score.pkl', 'wb') as f:
    pickle.dump(score, f)

with open('score.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)


# 예외처리
a, b = 10, 0

try:
    c = a / b
    if a > 10:
        raise ValueError('a 값은 10보다 작아야 합니다.')
except Exception as ex:
    print('0으로 나누었습니다.', ex)
else:
    print('결과값', c)
finally:
    print('연산이 완료되었습니다.')