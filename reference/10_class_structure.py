# Python Class Special Method advanced, heritage

# Class ABC

# Class define


import abc
import random
import sys


# class Bar(object, abc.ABC):
#     @abc.abstractmethod
#     def foo(self):
#         pass


class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        if y < 30:
            raise ValueError("y under 30 is not allowed")
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # Generator

    @property
    def x(self):
        print("Called Property x")
        return self.__x

    @x.setter
    def x(self, v):
        print("Called Property x Setter")
        self.__x = float(v)

    @property
    def y(self):
        print("Called Property y")
        return self.__y

    @y.setter
    def y(self, v):
        if v < 30:
            raise ValueError("y under 30 is not allowed")
        print("Called Property y Setter")
        self.__y = float(v)


# 객체 선언
v = VectorP(20, 40)

# print('EX 1-1 - ', v.__x, v.__y)

# Getter, Setter
print("EX 1-2 - ", dir(v), v.__dict__)

print("EX 1-3 - ", v.x, v.y)

# Iter 확인
for val in v:
    print("EX 1-4 - ", val)


# __slot__
# Python Interpreter에게 통보
# 해당 Class가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성 시 -> Memory 사용 공간 대폭 (감소 약 ~20%)
# Class에 만들어진 Instance 속성 관리에 Dict 대신 Set 자료형 사용


class TestA(object):
    __slots__ = ("a",)


class TestB(object):
    pass


use_slot = TestA()
no_slot = TestB()

print("EX 2-1 - ", use_slot)
# print('EX 2-2 - ', use_slot.__dict__)
print("EX 2-2 - ", no_slot)

print("EX 2-3 - ", no_slot.__dict__)


# Memory 사용량 비교
import timeit


# 측정 함수 선언


def repeat_outer(obj):
    def repeat_inner():
        obj.a = "TEST"
        del obj.a

    return repeat_inner()


# timeit.repeat(func(obj), number=10000)은 stmt error로 실행되지 않음 >> lambda로 function 지정
print("\n" + "-" * 100, "\n")
print("Using __slot__ >>>>>>>>")
print(min(timeit.repeat(lambda: repeat_outer(use_slot), number=500000)))
print("Not using __slot__ >>>>>>>>")
print(min(timeit.repeat(lambda: repeat_outer(no_slot), number=500000)))
print("\n" + "-" * 100, "\n")

print()


# Object Slicing


class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 100, 3)]

    # Method 구현
    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]


s = ObjectS()

print("EX 3-1 - ", s.__dict__)
print("EX 3-2 - ", len(s))
print("EX 3-3 - ", len(s._numbers))
print("EX 3-4 - ", s[0:100])
print("EX 3-5 - ", s[::10])

# Python 추상클래스
# ref : python foundation us docs

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 Instance를 생성해야 함
# 개발과 관련된 공통된 내용(field, Method) 추출 및 통합하여 공통된 내용으로 작성하게 하는 것
# ex. Phone -> Call, End, Battery Charge >>> Samsung Galaxy S21, Google Pixel 6, ..

# Sequence 상속 받지 않았지만, 자동으로 기능 작동
# object 전체를 자동으로 조사 -> Sequence Protocol


class IterTestA:  # 자동으로 __iter__, __contain__ 기능 상속/ getitem 상속했으므로 조사 후 자동으로 상속
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]


i1 = IterTestA()

print("EX 4-1 - ", i1[4])
print("EX 4-2 - ", i1[3:10])
print("EX 4-3 - ", 3 in i1[1:12])  # __contain__
# print('EX 4-4 - ', [i for i in i1])     # iterator
print()
print()


# Sequence 상속
# 요구사항인 ABS method를 모두 구현해야 동작


from collections.abc import Sequence


class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])


# Python이 어느 obj를 통해 for loop을 돌고자 할 때 다음과 같은 순서로 체크한다.
#
# __iter__가 제공되는지 체크하고, 있으면 이를 통해 iter(obj)를 사용하는 것으로 끝난다.
# 없다면 __getitem__이 있는지 체크하고, 있으면 index 0부터 시작해서 IndexError가 나올 때까지 __getitem__(index)를 호출해서 for loop을 제공한다.
# 이러한 일종의 규약 (protocol) 덕분에 __getitem__ 하나만 있으면 iterable type이 되고, 추가 코드 없이 아래와 같은 것들이 가능하다.
#
#
#
# 출처: https://dgkim5360.tistory.com/entry/python-duck-typing-and-protocols-why-is-len-built-in-function [개발새발로그]


i2 = IterTestB()

print("EX 4-5 - ", i2[4])
print("EX 4-6 - ", i2[3:10])
print("EX 4-7 - ", 3 in i2[1:12])
print([l for l in i2])
print("\n" + "-" * 100, "\n")
comp_list = [o for o in i2]
comp_tpl = (n for n in i2)
comp_set = {j for j in i2}
print("Comprehending list memory size - ", sys.getsizeof(comp_list))
print("Comprehending tuple memory size - ", sys.getsizeof(comp_tpl))
print("Comprehending set memory size - ", sys.getsizeof(comp_set))
print("\n" + "-" * 100, "\n")
print()


# abc 활용 예제
# import abc


class RandomMachine(abc.ABC):  # metaclass=abc.ABCMeta(under 3.4 version)
    # metaclass=abc.ABCMeta

    # Abstract Method
    @abc.abstractmethod
    def load(self, iterobj):
        """
        Iterable 항목 추가
        :param iterobj:
        :return:
        """

    # Abstract Method
    @abc.abstractmethod
    def pick(self, iterobj):
        """
        Randomly pick an obj
        :param iterobj:
        :return:
        """

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        return tuple(sorted(items))


# import random


class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)  # list에 추가
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()

        except IndexError:
            raise LookupError("Empty Crane Box")

    def __call__(self):
        return self.pick()

    # 메소드 오버라이드
    # def inspect(self):
    #     print('Override Test')


# Sub Class 확인
print("EX 5-1 - ", issubclass(RandomMachine, CraneMachine))
print("EX 5-2 - ", issubclass(CraneMachine, RandomMachine))

# Heritage 구조 확인
print("EX 5-3 - ", CraneMachine.__mro__)

cm = CraneMachine(range(1, 100))  # Abstract Method 구현 안하면 Error
# 상속 Class의 Method 구현을 강제하기 위해 Abstract Method 사용
# abc = Abstract Base Class


# 부모 Class를 보면 Sub Class의 내용도 일부 확인할 수 있음

print("EX 5-4 - ", cm._items)
print("EX 5-5 - ", cm.pick())
print("EX 5-6 - ", cm())
print("EX 5-7 - ", cm.inspect())
