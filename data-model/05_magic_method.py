# 05_magic_method.py
# Special Method
# ref1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# ref2 : https://www.tutorialsteacher.com/python/magic-methods-in-python
#
# Magic Method Prac

# Python sig part of Framework
# - > Sequence, Iterator, Functions, Class
import numpy as np

# Basic Type

print(int)  # 모든 datatype 은 object

# 모든 속성 및 Method 출력
print(dir(int))  # print(a for a in dir(int))
print()
print()

n = 100

# Usage
print("EX 1-1 - ", n + 200)
print("EX 1-2 - ", n.__add__(200))
print("EX 1-3 - ", n.__doc__)
print("EX 1-4 - ", n.__bool__(), bool(n))
print("EX 1-5 - ", n * 100, n.__mul__(100))

print()
print()


# Class 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return "Student Class Info : {}, {}".format(self._name, self._height)

    def __le__(self, x):
        print("Called. >> __le__ Method.")
        if self._height <= x._height:
            return True
        # 추가 static/class/instance method 구현,
        # 웹에 x에 대한 정보 전송 등 다양한 활용
        else:
            return False

    def __sub__(self, x):
        print("Called. >> __sub__ Method.")
        return abs(self._height - x._height)


s1 = Student("James", 180)
s2 = Student("Mie", 165)

# Magic Method Output
print("EX 2-1 - ", s1 >= s2)
print("EX 2-2 - ", s1 - s2)
print("EX 2-3 - ", s1)

# Class 예제2

# 벡터(Vector) numpy


class Vector(object):
    def __init__(self, *args):  # Unpacking tuple
        """
        Create a vector
        ex : v = Vector(1, 2)
        :param args: v = Vector(1, 2)
        """

        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """Returns the vector information"""
        return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other):
        """Returns the vectors' addition result of self and others"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        """Returns the vectors' mul result of self and others"""
        return self._x * other._x, self._y * other._y

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector Instance 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()
v4 = Vector(-2, -7)

# Magic Method Output
print("EX 3-1 - ", Vector.__init__.__doc__)
print("EX 3-2 - ", Vector.__repr__.__doc__)
print("EX 3-3 - ", Vector.__add__.__doc__)
print("EX 3-4 - ", v1, v2, v3, v4)

print("EX 3-5 - ", v1 + v2)
print("EX 3-6 - ", v1 * v2)
print("EX 3-7 - ", bool(v1))
print("EX 3-7 - ", bool(v4))

# Numpy
V_01 = np.array([1, 2])
V_02 = np.array([1, 4])

# Numpy Output
print(V_01.dot(V_02))
print(np.dot(V_01, V_02))
