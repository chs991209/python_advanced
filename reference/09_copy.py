# 객체 참조의 중요한 특징
# Python Object Reference

print('EX 1-1 - ')
print(dir(__name__))    # 속성 값 Check

# id vs __eq__ 증명
x = {
    'name': 'kim',
    'age': 33,
    'city': 'Seoul',
}
y = x
print('EX 2-1 - ', id(x), id(y))    # Effeciency 때문
print('EX 2-2 - ', x == y)
print('EX 2-3 - ', x is y)  # id 값 equivalent
print('EX 2-4 - ', f'{x}, {y}')

# 대입받을 param의 값을 변경하면 대입된 param의 값도 변한다.
x['class'] = 10
print('EX 2-5 - ', x, y)

print()
print()

z = x = {
    'name': 'kim',
    'age': 33,
    'city': 'Seoul',
    'class': 10
}

print('EX 2-6 - ', x, z)
print('EX 2-7 - ', x is z)  # 같은 객체
print('EX 2-8 - ', x is not z)
print('EX 2-9 - ', x == z)  # 같은 값

# 객체 생성 후 Immutable -> 즉, ID는 객체의 주소(정체성) 비교, == (__eq__) 는 값을 비교
# 자료의 값을 비교하면 모든 값을 다 비교해야 하므로 시간이 오래 걸린다. 따라서 id부터 비교하고, 같다면 값도 같다는 것을 알 수 있다.

tuple1 = (10, 15, [100, 500])
tuple2 = (10, 15, [100, 500])

print('EX 3-1 - ', id(tuple1), id(tuple2))
print('EX 3-2 - ', tuple1 is tuple2)
print('EX 3-3 - ', tuple1 == tuple2)
print('EX 3-4 - ', tuple1.__eq__(tuple2))

print('\n' + ('-' * 100), '\n')

# Copy, Deepcopy (깊은 복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)     # 복사


print('EX 4-1 - ', tl1 == tl2)
print('EX 4-2 - ', tl1 is tl2)
print('EX 4-3 - ', tl1 == tl3)
print('EX 4-4 - ', tl1 is tl3)


# 증명
print('EX 4-7 - ', tl3)
tl1.append(1000)
tl1[1].remove(105)

print('EX 4-5 - ', tl1)
print('EX 4-6 - ', tl2)
print('EX 4-7 - ', tl3)

print()

# print(id(tl1[2]))
tl1[1] += [110, 120]
tl2[2] += (100, 125)    # tuple 데이터 메모리 재할당, 새로운 객체 생성하므로 성능, 비용 문제가 생김.

print('EX 4-8 - ', tl1)
print('EX 4-9 - ', tl2)
print('EX 4-10 - ', tl3)
# print(id(tl1[2]))


# Deep Copy

class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def add_prod(self, prod_name):
        self._products.append(prod_name)

    def sub_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Basket(['apple', 'backpack', 'snickers', 'bottle'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX 5-1 - ', id(basket1), id(basket2), id(basket3))
print('EX 5-2 - ', id(basket1._products), id(basket2._products), id(basket3._products))
# deepcopy는 내부 variable들을 복사한다 (재할당)

# 증명
basket1.add_prod('Orange')
basket2.sub_prod('snickers')

print('EX 5-3 - ', basket1._products)
print('EX 5-4 - ', basket2._products)
print('EX 5-5 - ', basket3._products)


# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    # x = x + y
    return x


x = 10
y = 5

print('EX 6-1 - ', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]

print('EX 6-2 - ', mul(a, b), a, b)     # 가변형 (Mutable) 자료형은 id 값도 전달된다 -> local에서 선언/재할당하지 않아도 값이 변경됨

c = (10, 100)
d = (5, 10)

print('EX 6-3 - ', mul(c, d), c, d)     # 불변형 (Immutable)


# Python 불변형 예외
# str, bytes, frozenset, Tuple: 사본 생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX 7-1 - ', tt1 is tt2, id(tt1), id(tt2))    # ref 반환
print('EX 7-2 - ', tt3 is tt1, id(tt3), id(tt1))    # ref 반환

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX 7-3 - ', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX 7-4 - ', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))



