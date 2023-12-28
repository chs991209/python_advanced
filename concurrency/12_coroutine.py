# Concurrency

# Coroutine
# -> yield: Main routine <-> sub routine
# yield from

# sub routine은 main routine에서 return에 의해서, sub routine call 부분으로 돌아와 다시 process 실행
# Coroutine : routine 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 process 실행 -> 탈출부를 나가지 않고 분할해서 실행 가능
# -> 동시성 프로그래밍 가능화
# Scheduling Overhead (스케줄링 오버헤드)와 같은 서버의 메모리 낭비가 매우 적음.
# 단점: 가독성이 떨어짐
# threading : Single -> Multi -> Complex -> Shared resource -> Stuck status 발생 가능성
# ex. 브라우저의 멀티 threads 작업
# context switching 비용 발생, resource 소비 가능성 증가

# Coroutine의 Basic Structure -> Coroutine의 단점 체크


def coroutine1():
    print(">>> Coroutine Began")
    i = yield

    # 비동기적 실행
    print(">>> Coroutine Value Received >>> {}".format(i))


c1 = coroutine1()

print("EX 1-1 - ", c1, type(c1))

# yield 실행 전까지 진행


# next(c1) -> 부가 호출 -> coroutine에서
# 부가 호출 -> none

# generator에 맵핑된 값 전달
# c1.send(100)  yield에 대기하지 않은, 함수 process 대기 상태에서 error 발생

# GEN_CREATED : 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태 -> yield

from inspect import getgeneratorstate


def coroutine2(x):
    print(">>> coroutine began : {}".format(x))
    y = yield x
    print(">>> coroutine received : {}".format(y))
    z = yield x + y
    print("coroutine received : {}".format(z))


c3 = coroutine2(10)

print(getgeneratorstate(c3))

print(next(c3))

print(getgeneratorstate(c3))
print(c3.send(15))  # y에 15를 send
print()
print()
# print(c3.send(15))    StopIteration Exception

# Decorator

from functools import wraps


def coroutine(func):
    """
    Decorator run until yield
    :param func:
    :return:
    """

    @wraps(func)  # 주석 등을 가져옴
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def createsum():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = createsum()

"""
중첩 Coroutine 처리를 하자.
"""


# def gen1():
#     for x in "AB":
#         yield x
#     for k in "Alphabet":
#         yield k
#
def gen1():
    yield from "AB"
    yield from "Alphabet"


test1 = gen1()

print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))
print(list(gen1()))
# print(getgeneratorstate(test1))
