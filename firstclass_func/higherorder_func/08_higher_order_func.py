# 08_higher_order_func.py
# First class functions(일급 객체)
# Python Functions의 특징
# 1. runtime 초기화 가능
# 2. 변수 등에 할당 가능
# 3. 함수에 인수로 전달 가능 ex. sorted(keys=len)
# 4. Function 결과로 반환 가능  ex. return func

import random

# ex Go, JavaScript, Reactjs, Angular -> 함수를 객체 취급> 함수형 프로그래밍 언어
from dis import dis
from inspect import signature


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

from operator import mul
from functools import partial

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
#
from collections import OrderedDict

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

# Closure (클로저)
#

a = 10

print("EX 2-1 - ", a + 10)
print("EX 2-2 - ", a + 100)

# 결과 누적
print("EX 2-3 ", reduce(add, [10, 100], 10))
print("EX 2-4 ", sum([10, 100]))

print()
print()


# Class 이용
class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)

        print("class >>> {} / {}".format(self._series, len(self._series)))

        return sum(self._series) / len(self._series)


# Instance 생성
avg_cls = Averager()

# 누적 확인
print("EX 3-1 - ", avg_cls(15))
print("EX 3-2 - ", avg_cls(35))
print("EX 3-3 - ", avg_cls(40))


print()
print()


# Closure 사용


def closure_avg1():
    """
    전역 변수 사용 감소
    Design Pattern에 적용
    변수 캡슐화 가능
    마우스 클릭 데이터 등을 누적할 때 사용

    데이터를 함수 외부에 많이 축적하여 resource를 잡아 먹을 수 있음
    """

    # Free variable area
    series = []
    # Closure area

    def averager(v):
        series.append(v)
        print("def1 >>> {} / {}".format(series, len(series)))

        return sum(series) / len(series)

    return averager


avg_closure1 = closure_avg1()

print("EX 4-1 - ", avg_closure1)
print("EX 4-2 - ", avg_closure1(14))
print("EX 4-3 - ", avg_closure1(30))

print()
print()

print("EX 5-1 - ", sorted(dir(avg_closure1)))
print()
print("EX 5-2 - ", sorted(dir(avg_closure1.__code__), reverse=True))
print()
print("EX 5-3 - ", avg_closure1.__code__.co_freevars)
print()
print("EX 5-4- ", sorted(dir(avg_closure1.__closure__[0].cell_contents)))

print()
print()


# Inappropriate Closure Usage


def closure_avg2():
    # Free Variable Area
    cnt = 0
    total = 0
    # Closure Area

    def averager1(v):
        # nonlocal cnt, total 주석 해제 후 실행
        nonlocal cnt, total
        cnt += 1
        total += v
        print("def1 >>> {} / {}".format(total, cnt))

        return total / cnt

    return averager1


avg_closure2 = closure_avg2()

print("EX 5-5 - ", avg_closure2(14))
print("EX 5-6 - ", avg_closure2(16))


# Decorator Prac
# closure와 비슷한 기능을 하지만, closure와 코드를 다르게 작성해도 된다.
# 1. 중복 제거, 코드 간결화
# 2. closure보다 간결한 문법
# 3. 조합해서 사용하기에 용이함

# 단점
# 1. debuging이 어려움
# 2. Error 발생 지점 추적이 어려움
# 3. IDEA의 도움으로 단점 해결 가능


import time


def perf_clock(func):
    def perf_clocked(*args):
        # Initial timestamp
        st = time.perf_counter()
        result = func(*args)
        # End timestamp
        et = time.perf_counter() - st
        # Function Name
        title = func.__name__
        # 매개변수
        args_str = ", ".join(repr(arg) for arg in args)
        # Output
        print("Result : [%0.5fs] %s(%s) -> %r" % (et, title, args_str, result))
        return result

    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n - 1)


# Decorate 미사용

# non_deco1 = perf_clock(time_func)
# non_deco2 = perf_clock(sum_func)
# non_deco3 = perf_clock(fact_func)
#
# print('EX 7-1 - ', non_deco1, non_deco1.__code__.co_freevars)
# print('EX 7-2 - ', non_deco2, non_deco2.__code__.co_freevars)
# print('EX 7-3 - ', non_deco3, non_deco3.__code__.co_freevars)
#
# print('*' * 40, 'Called Non Decorator -> time_func')
# print('EX 7-4 - ')
# non_deco1(2)
#
# print('*' * 40, 'Called Non Decorator -> sum_func')
# print('EX 7-5 - ')
# non_deco2(1, 2, 5, 10)
#
# print('*' * 40, 'Called Non Decorator -> fact_func')
# print('EX 7-6 - ')
# non_deco3(10)

# print()
# print()
# print()
# # print(sorted(dir(non_deco1)))
# # print(sorted(dir(non_deco2)))
# # print(sorted(dir(non_deco3)))

print("*" * 40, "Called Non Decorator -> time_func")
print("EX 7-7 - ")
time_func(2)

print("*" * 40, "Called Non Decorator -> sum_func")
print("EX 7-8 - ")
sum_func(1, 2, 5, 10)

print("*" * 40, "Called Non Decorator -> fact_func")
print("EX 7-9 - ")
fact_func(3)

# 회원 탈퇴
# 유료 캐시가 남아 있는지, .. 등을 체크해
# 어떠한 조치를 취해야 하는 지 등을 decorator로 작성
