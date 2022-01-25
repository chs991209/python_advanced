# 08_1_closure_decorator.py
# Closure (클로저)

# 파이썬 변수 범위(global)

import time
from dis import dis
from functools import reduce
from operator import add


# 예제1
def func_v1(a):
    print(a)
    print(b)


# 예외
# func_v1(5)


# 예제2
b = 10


def func_v2(a):
    print(a)
    print(b)


func_v2(5)


# 예제3
# 예제2
b = 10


def func_v3(a):
    # global b
    print(a)
    print(b)
    b = 20


# func_v3(5)

# from dis import dis

print("EX1-1 -")
print(dis(func_v3))

print()
print()


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
