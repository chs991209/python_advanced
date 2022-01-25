# 08_higher_order_func.py
# First class functions(일급 객체)
# Python Functions의 특징
# 1. runtime 초기화 가능
# 2. 변수 등에 할당 가능
# 3. 함수에 인수로 전달 가능 ex. sorted(keys=len)
# 4. Function 결과로 반환 가능  ex. return func

# ex Go, JavaScript, Reactjs, Angular -> 함수를 객체 취급> 함수형 프로그래밍 언어

import random
from collections import OrderedDict
from dis import dis
from functools import partial
from inspect import signature
from operator import mul


def factorial(n):
    """
    Factorial function -> n:int
    :param n:
    :return:
    """

    if n == 1:  # n < 2
        return 1
    return n * factorial(n - 1)


class A:
    pass


print("EX 1-1 - ", factorial(5))
print("EX 1-2 - ", factorial.__doc__)
print("EX 1-3 - ", type(factorial), type(A))
print("EX 1-4 - ", dir(factorial))
print("EX 1-5 - ", dir(A))

# print('EX 1-6 - ', set(sorted(dir(factorial))) - set(sorted(dir(A))))
print("EX 1-6 - ", set(dir(factorial)) - set(dir(A)))
print("EX 1-7 - ", sorted(list(set(dir(factorial)) - set(dir(A))), key=len))
print("EX 1-8 - ", factorial.__get__)
print("EX 1-9 - ", factorial.__code__)
print("EX 1-10 - ", factorial.__closure__)
print("EX 1-11 - ", factorial.__name__)

# 변수 할당
var_func = factorial

print("\n" + "-" * 100, "\n")
print("EX 2-1 - ", var_func)
print("EX 2-2 - ", var_func(7))
print("EX 2-3 - ", map(var_func, range(1, 6)))
print("EX 2-4 - ", list(map(var_func, range(1, 6))))

# 함수 인수 전달 (포함), return func -> Higher-order Function

print("EX 3-1 - ", list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print("EX 3-2 - ", list(map(var_func, filter(lambda x: x > 4, range(1, 6)))))
print("EX 3-3 - ", [var_func(i) for i in range(1, 6) if bool(i % 2) is True])

print()
# reduce()

from functools import reduce
from operator import add

values_list = [1, 2, 3, 4]
print("EX 3-3 - ", reduce(add, range(1, 11)))
print("EX 3-4 - ", sum(range(1, 11)))
print("EX 3-5 - ", reduce(lambda x, y: x + y, values_list, 0))

# 익명 함수 (lambda)
# 가급적 주석 ref 사용
# 가급적 일반 함수 사용
# 일반 함수로 refactoring 하는 것을 권장

print("EX 3-6", reduce(lambda x, t: x + t, range(1, 11)))

print(dis("range(1, 11)"))

# Callable : 호출 연산자 -> Method 형태로 Callable한지 확인


# Lotto 추첨 Class define
class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __hash__(self) -> int:
        return super().__hash__()

    def __call__(self, *args, **kwargs):
        return self.pick()


print("Doc random.choice: ", random.choice.__doc__)

# object 생성
game_0119 = LottoGame()


# from data_model.data_model_test.test_namedtuple import StudentCode
# Game Play
print(
    "EX 4-1 - ",
    callable(str),
    callable(list),
    callable(factorial),
    callable(3.14),
    callable(random.choice),
    callable(hash),
    callable(game_0119),
)
print("EX 4-2 - ", game_0119.pick())

print("EX 4-3 - ", game_0119())


print("LottoGame dir - ", dir(LottoGame))

print()
print()

# Various Params (*args, **kwargs)
# packing * >> tuple, ** >> dict


def args_test(name, *contents, point=None, **attribs):
    return "<args_test> -> ({}) ({}) ({}) ({})".format(name, contents, point, attribs)


print("EX 5-1 - ", args_test("test1"))
print("EX 5-2 - ", args_test("test1", "test2"))
print("EX 5-3 - ", args_test("test1", "test2", "test3", id="admin"))
print("EX 5-4 - ", args_test("test1", "test2", "test3", id="admin", point=7))
print(
    "EX 5-5 - ",
    args_test("test1", "test2", "test3", id="admin", point=7, password="Easy"),
)

print()
print()

# Function Signatures
# inspect 패키지 중 signature 사용 >> signature 사용 빈도 낮음/ 로컬 사용

sg = signature(args_test)

print("EX 6-1 - ", sg)
print("EX 6-2 - ", sg.parameters)

print()

# 모든 Info 출력

for name, param in sg.parameters.items():
    print("EX 6-3 - ", name, param.kind, param.default)

print()
print()

# partial Usage: Instance 고정, 새로운 func return- > 주로 특정 Instance fix 후 callback func에 사용
# 이미 한 개 이상의 인수를 할당받은 함수를 return
# 함수의 새로운 return된 형식 type은 기본 함수 자체를 기술하고 있음

# import operator.mul
# import functools.partial

print("EX 7-1 - ", mul(10, 27))

# 인수 고정
five = partial(mul, 5)

oneplus = partial(add, 1)

print(oneplus(1))

# fix 추가
six = partial(mul, 6)

print("EX 7-2 - ", five(100), six(120))
print("EX 7-3 - ", [five(i) for i in range(1, 11)])
print("EX 7-4 - ", list(map(five, range(1, 11))))


# OrderedDict >> 추가 code sample
# OrderedDict는 dict class를 상속받은, 하나의 class

# import collections.OrderedDict

name_script = OrderedDict[("name", "myname"), ("yname", "yourname")]
print(name_script)
print(type(name_script))
name_script_1 = OrderedDict[("yname", "yourname"), ("name", "myname")]

if name_script == name_script_1:
    print("Identical")
else:
    print("Not Identical")

# OrderedDict 클래스와 dict(자료형 class)의 Method 차이를 check

# OrderedDict/ dict 의 dir
print(dir(OrderedDict))
print(dir(dict))
# dir의 차이
# set으로 구분
print(set(sorted(dir(OrderedDict))) - set(sorted(dir(dict))))

if "__dict__" in dir(dict):
    print("Yes, __dict__ is involved")

else:
    print("No, __dict__ is not involved")

print("-" * 100)

if "__dict__" in dir(int):
    print("Yes, __dict__ is involved")

else:
    print("NO")

print("-" * 100)

name_script_list = ["a", "b", "cc", "d", "ee"]

sorted_name_script = name_script_list.sort(key=len)
print(sorted_name_script)
print(name_script_list)

sorted_name_script = name_script_list.sort(key=len, reverse=True)

print(name_script_list)
print()
print()
