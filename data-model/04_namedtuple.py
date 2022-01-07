# Python Data Model
# 04_namedtuple.py
# ref : https://docs.python.org/3/reference/datamodel.html

# Namdedtuple Prac

# Python 의 sig framework
# -> 시퀀스 Sequence, 반복 Iterator, 함수 Functions, 클래스 Class

from collections import namedtuple
from math import sqrt  # Namedtuple 사용

# Object -> Python 의 data 를 추상화
# 모든 Object-> id, type -> value  (메모리)
# Python 은 일관성이 있음
# sqrt - rout

# General Tuple 과 Namedtuple 의 차이

# General Tuple
# 0 : x , 1: y

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

print("\n",
      ("-" * 100),
      "\n")

line_len1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print("EX 1-1 - ", line_len1)

# Namedtuple 사용

# Namedtuple 선언
# Cls
Point1 = namedtuple("Point", "x, y")

# 두 점 선언
pt1 = Point1(1.0, 5.0)
pt2 = Point1(2.5, 1.5)

# 계산
line_len2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# Output
print("\nEX 1-2 - ", line_len2)
print("\nEX 1-3 - ", line_len1 == line_len2)

# Namedtuple 선언 방법 ("cls_name", list or string with comma or etc)
Point1 = namedtuple("Point", ["x", "y"])  # list
Point2 = namedtuple("Point", "x, y")  # Comma
Point3 = namedtuple("Point", "x y")  # blank

# 띄어쓰기보다 list, .. 방식을 선호함
# 4개의 변수를 갖는 방식 >> rename = True 면 새로운 변수 namespace 의 name 을 Interpreter 가 읽을 때 랜덤으로 만듦 >> Error 방지

Point4 = namedtuple(
    "Point", "x y x class", rename=True
)  # 같은 key가 중복되거나, 예약어(class)를 사용하는 경우

# Dict to Unpacking
dict_ex = {"x": 30, "y": 350}

# 출력

print("\n" + str("-" * 100) + "\n")
print("EX 2-1 - ", Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

# 객체 생성 - Dict Unpacking
# **는 dict의 앞에 붙여 unpacking 함
p5 = Point3(**dict_ex)

# 출력

print()
print(
    "EX 2-2\n",
    "\np1 : {}\np2 : {}\np3 : {}\np4 : {}\np5 : {}".format(
        p1, p2, p3, p4, p5
    ),
)
print()
print(
    "EX 2-3\n",
    "\np1 : {}\np2 : {}\np3 : {}\np4 : {}\np5 : {}".format(
        p1.__repr__(),
        p2.__repr__(),
        p3.__repr__(),
        p4.__repr__(),
        p5.__repr__(),
    ),
)
print("\n" + str("-" * 100) + "\n")

# index 호출 (Namedtuple)
print(
    "EX 3 -1 -",
    "{}\n{}".format(
        (p1[0] + p2[0]), "== p1.[0] + p2[0]" + "\n\nClass Variable call works\n"
    ),
)  # Index Error 타이핑 주의
print(
    "EX 3 -2 -", "{}\n{}".format((p1.x + p2.x), "== p1.x + p2.x")
)  # Class Variable 접근 방식
print()

# Unpacking
x, y = p3

print("EX 3-3 -", x + y)
print()

# Rename Test
print("EX 4-4 -", p4)
print("\n",
      ("-" * 100),
      "\n")

# Namedtuple Methods

temp = [52, 38]

# _make() Method : 새로운 객체 생성
p4 = Point1._make(temp)
print("EX 4-1 - ", p4)

# _fields : Check Field Name
print("EX 4-2 - ", p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print("EX 4-3 - ", p1._asdict(), p2._asdict(), p3._asdict())

# _replace() : 수정된 새로운 객체 반환
p2_mod = p2._replace(y=100)

print("EX 4-4 - ", p2_mod)
print("\n",
      ("-" * 100),
      "\n")

# 실 사용 실습
# 학생 전체 그룹 생성
# 1반에 20명, 4개의 반 -> (A, B, C, D)

# Namedtuple 선언
Classes = namedtuple("Classes", ["rank", "number"])

# Group List 선언
# 지능형 List - List Comprehension
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D ".split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print("EX 5-1 - ", len(students))
print("EX 5-2 - ", students[0].number)  # dict와 비슷한 방식으로 call 할 수 있다.
print("\n",
      ("-" * 100),
      "\n")

# 가독성 X

students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]

students3 = [
    Classes(rank, number)
            for rank in "A B C D".split()
                for number in [str(n)
                    for n in range(1, 21)]]   #계층식

print("EX 6-1 - ", len(students2))
print("EX 6-2 - ", students2[0].number)

print("\n",
      ("-" * 100),
      "\n")

# Output
for s in students:
    print("EX 7-1 - ", s)
