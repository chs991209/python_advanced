# Python sequence
# 해시테이블 (Hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 x
# Dict 및 Set Advanced
import csv
import timeit
from dis import dis

# import sys
# import io
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# Dict 구조
print("EX 1-1 - ")
# print(__builtins__.__dict__)

print("\n", "-" * 100, "\n")

# Hash 값 확인
t1 = (
    10,
    20,
    (30, 40, 50),
)
t2 = (
    10,
    20,
    [30, 40, 50],
)

print("EX 1-2 - ", hash(t1))
# print('EX 1-3 - ', hash(t2))


# list는 unhashable(가변적)
# print('EX 1-2 - ', hash(t2))

# 지능형 Dictionary (Comprehending Dict)

# 외부 csv to List of Tuple

with open(
    "C:/Users/chs99/문서/Pycharm Projects/resources/test1.csv", "r", encoding="UTF-8"
) as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print(
    "EX 2-1 - ",
)
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print(
    "EX 2-2 - ",
)
print(n_code1)

print()
print()

print(
    "EX 2-3 - ",
)
print(n_code2)

# Dict Setdefault sample

source = (
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5"),
)

new_dict1 = {}

# Not using setdefault

# key는 중복시키지 않고,
# value들을 sequence 형태의 list들로 생성함.

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print("EX 3-1 - ", new_dict1)

# Using setdefault
new_dict2 = {}

for k1, v1 in source:
    new_dict2.setdefault(k1, []).append(v1)

print("EX 3-2 - ", new_dict2)


# User defined dict 상속(UserDict 가능)

# (dict) > dict에 내장된 관련 Method 들을 상속받음
class UserDict(dict):
    # key가 dict 내의 없을 때
    def __missing__(self, key):
        print("Called : __missing__")
        # key 값 형태 비교
        if isinstance(key, str):
            raise KeyError(key)

        return self[str(key)]

    # get method로 dict의 value 꺼내기
    def get(self, key, default=None):
        print("Called : __getitems__")
        try:
            return self[key]
        except KeyError:
            return default

    # in 연산자로 값이 맞는 지 확인
    def __contains__(self, key):
        print("Called : __contains__")
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({"one": 1, "two": 2})
user_dict3 = UserDict([("one", 1), ("two", 2)])
# 출력
print("EX 4-1 - ", user_dict1, user_dict2, user_dict3)
print("EX 4-2 - ", user_dict2.get("two"))
print("EX 4-3 - ", "one" in user_dict3)
# print('EX 4-4 - ', user_dict3['three'])
# __missing__
print("EX 4-5 - ", user_dict3.get("n"))
print("EX 4-6 - ", "three" in user_dict3)
print()
print()


# Timeit
# 자료형 속도 비교하기
print("\n", "-" * 100, "\n")

test1 = """
for k1, v1 in source:
    new_dict2.setdefault(k1, []).append(v1)
"""

print(
    timeit.timeit(
        test1,
        setup="""
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),

    )

new_dict2 = {}
        """,
        number=1000,
    )
)

print()
print()

test2 = """
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
"""

print(
    timeit.timeit(
        test2,
        setup="""
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
    ('k2', 'val6'),
    ('k3', 'val5'),
    ('k3', 'val7'),
    ('k3', 'val8'),
    ('k3', 'val9'),
    )

new_dict1 = {}
""",
        number=1000,
    )
)

print("\n", "-" * 100, "\n")


# Immutable Dict

# MappingProxyType

from types import MappingProxyType

d = {"key1": "TEST1"}

# Read Only
d_frozen = MappingProxyType(d)
print("EX 5-1 - ", d, id(d))
print("EX 5-2 - ", d, id(d_frozen))
print("EX 5-3 - ", d is d_frozen, d == d_frozen)

# d_frozen['key1'] = 'TEST2'
# TypeError: 'mappingproxy' object does not support item assignment
# 수정 불가 (Immutable)

d["key2"] = "TEST2"

print("EX 5-4 - ", d)


# Set 구조 (FrozenSet)
# Set은 미리 정제된 데이터를 사용하는 것이 좋음(중복 알고리즘 처리 시간 상승)

s1_contact_co = {"Apple", "Samsung", "Pfizer", "Huawei", "Hynix"}
s2_contact_co = set(["Apple", "Pfizer", "Huawei", "Hynix", "Samsung"])
s3 = {3}

set_empty = set()

s5_frozen_contact_co = frozenset({"Apple", "Samsung", "Pfizer", "Huawei", "Hynix"})


# Add
s1_contact_co.add("Xiami")

# Unable to Add
# s5_frozen_contact_co.add('Audi')

print("EX 6-1 - ", s1_contact_co, type(s1_contact_co))
print("EX 6-2 - ", s2_contact_co, type(s2_contact_co))
print("EX 6-3 - ", s3, type(s3))
print("EX 6-4 - ", set_empty, type(set_empty))
print("EX 6-5 - ", s5_frozen_contact_co, type(s5_frozen_contact_co))

# 선언 최적화

print("EX 6-5 - ")
print(dis("{3, 5, 6}"))
print("EX 6-6 - ")
print(dis("set([3, 5, 6])"))
print()
print()

# 지능형 집합 (Comprehending Set)
from unicodedata import name

print("EX 7-1 - ")

print({chr(i) for i in range(0, 256)})
print({name(chr(i), "") for i in range(0, 256)})
