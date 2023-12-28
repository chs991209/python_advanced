# 11_generator.py
# 흐름 제어, 병행 처리 (Concurrency)

# Generator, 반복형

# Python 반복형 종류
# for, collections, text file, list, Dict, Set, Tuple, unpacking (*), *args

# 반복형 객체의 내부적인 iter 함수 내용, Generator 동작 원리, yield from

# Iterable 한 이유 -> iter(x) 함수 호출


from collections import abc


t = "ABCDEF"


# for Usage
for c in t:
    print("EX 1-1 - ", c)

print()

# while Usage

w = iter(t)

while True:
    try:
        print("EX 1-2 - ", next(w))
    except StopIteration as log:
        print(log)
        break


# Iterable 한 지 확인
print("EX 1-3 - ", hasattr(t, "__iter__"))
print("EX 1-4 - ", isinstance(t, abc.Iterable))

print()
print()

# next 사용


class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        # print("Called __next__")
        try:
            word = self._text[self._idx]

        except IndexError:
            raise StopIteration("Stop calling generator; Iterable is Exhausted ")

        self._idx += 1

        return word

    def __iter__(self):
        print("Called __iter__")
        return self

    def __repr__(self):
        return "WrodSplit(%s)" % (self._text)


wi = WordSplitIter("Who said that the novel is so thick?")

print("EX 2-1 - ", wi)
print("EX 2-2 - ", next(wi))
print("EX 2-3 - ", next(wi))
print("EX 2-4 - ", next(wi))
print("EX 2-5 - ", next(wi))
print("EX 2-6 - ", next(wi))
print("EX 2-7 - ", next(wi))
print("EX 2-8 - ", next(wi))
print("EX 2-9 - ", next(wi))
# print("EX 2-10 - ", next(wi))
print()
print()

# Generator Pattern
# 1. Comprehending List, Dict, Set -> Data Set이 증가할 경우 Memory 사용량 증가 -> Generator가 완화
# 2. Unit 실행 가능한 Coroutine에 아주 중요
# 3. Dict, List 한 번 호출 할 때마다 하나의 값만 return -> 아주 작은 메모리 양을 요구함
# ex) 게시판의 글 내용을 호출될 때만 return 함


class WordSplitGenerator:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word  # Generator

    def __repr__(self):
        return "WordSplit(%s)" % (self._text)


wg = WordSplitGenerator("Who said that the novel is so thick?")

wt = iter(wg)

print("EX 3-1 - ", wt)
print("EX 3-2 - ", next(wt))
print("EX 3-3 - ", next(wt))
print("EX 3-4 - ", next(wt))
print("EX 3-5 - ", next(wt))
print("EX 3-6 - ", next(wt))
print("EX 3-7 - ", next(wt))
print("EX 3-8 - ", next(wt))
print("EX 3-9 - ", next(wt))
# print("EX 3-10 - ", next(wt))
print()
print()

# Generator 예제 1


def generator_ex1():
    print("Get Strated")
    yield "AAA"
    print("continue")
    yield "BBB"
    print("The End")


temp = iter(generator_ex1())

# print('EX 4-1 - ', next(temp))
# print('EX 4-2 - ', next(temp))
# # print('EX 4-3 - ', next(temp))  # StopIteration Error

# for 문으로 next 호출
# for v in generator_ex1():
#     print('EX 4-3 - ', v)


# Generator 예제2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print("EX 5-1 - ", temp2)
print("EX 5-2 - ", temp3)
for i in temp2:
    print("EX 5-3 - ", i)

temp_list = []

for i in temp3:
    print("EX 5-4 - ", i)


# Generator Ex 3
# 자주 사용하는 func

import itertools

gen1 = itertools.count(1, 2.5)
print("EX 6-1 - ", next(gen1))
print("EX 6-2 - ", next(gen1))
print("EX 6-3 - ", next(gen1))
# 무한

# 조건 (itertools.takewhile())

# takewhile(pred=, seq=)

print()

gen2 = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2.5))

for v in gen2:
    print("EX 6-5 - ", v)

#
# def gen2_over(pred, data):
#     for x in data:
#         if pred(x):
#             yield x
#         else:
#             break
#
## print(next(gen2_over(lambda x: x < 11, itertools.count(1, 2.5))))


print()

# Filter와 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print("EX 6-6 - ", v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 11, 1)])

# idx = 0
# for v in gen4:
#     idx += 1
#     print('EX 6-{} - {}'.format(idx, v))
print()
for v in gen4:
    print("EX 6-7 - ", v)

print()

# 연결 1
gen5 = itertools.chain("ABCDE", range(1, 11, 2))


print("EX 6-8 - ", list(gen5))
# gen6 = itertools.chain('ABCDE', range(1, 11, 2))
# for k in gen6:
#     print(k)

# 연결 2
gen6 = itertools.chain(enumerate("ABCDE"))
print("EX 6-9 - ", list(gen6))  # packing

# 개별
gen7 = itertools.product("ABCDE")
print("EX 6-10 - ", list(gen7))

# 연산 generator to list(repeat -> 중복 조합 원소 수)
gen8 = itertools.product("ABCDE", repeat=2)
print("EX 6-11 - ", list(gen8))
gen8_1 = itertools.product(["a", "b", "c"], repeat=2)
gen8_2 = itertools.product(["a", "b", "c"], repeat=3)

print()
print("EX 6-11-1 - ", list(gen8_1))
print()
# print(tuple(gen10))
dict_sample = {}
for k, v in enumerate(gen8_2):
    dict_sample[k] = v
print("EX 6-11-2 - ", dict_sample)

# Groupby
gen9 = itertools.groupby("AAABBCCCCDDEEEEE")
# print('EX 6-12 - ', list(gen9))
#
# for chr, group in gen9:
#     print(chr, ":", tuple(group))


def groupby(gen):
    a = [(chr, list(group)) for chr, group in gen]
    return a


import timeit

print(timeit.timeit("groupby(gen9)", number=1000, globals=globals()))


gen10 = itertools.groupby([0, 0, 0, 0, 1, 2, 2, 3, 1, 1])
print("-----------------")
for chr, group in gen10:
    print(chr, ":", list(group))

a = [0, 0, 0, 0, 1, 2, 2, 3, 1, 1]
b = ({k: a.count(k)} for k in set(a))
for j in b:
    print(j)
