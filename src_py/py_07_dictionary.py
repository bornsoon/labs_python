"""
Dictionary
 - 가변형
 - key, value (key:불변형, value:가변형)
 - 순서가 없다.
 - 중복키는 허용되지 않는다.(수정된다.)
"""

a = {"name": "Full HD TV", "price": 1000000, "제조국": "대한민국", "price": 110000}
print(a)
print(a["name"], a["제조국"])

b = dict([("name", "Full HD TV"), ("price", 1000000), ("제조국", "대한민국"), ("price", 110000)])
print(b)

c = {("name", "price", "제조국"):("Full HD TV", 1000000, "대한민국")}
print(c)
print(c[("name", "price", "제조국")])
print(c[("name", "price", "제조국")][0])

# 메소드
print(a.get('name'))
# print(a['maker'])   # 없는 키값은 오류 발생
print(a.get('maker', '없음'))
print(a.values(), list(a.values()))

# zip
keys = ("name", "price", "제조국")
values = ("Full HD TV", 1000000, "대한민국")

print(list(zip(keys, values)))
print(dict(zip(keys, values)))