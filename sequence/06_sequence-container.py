# sequence container

# Sequence 형

# Container : 서로 다른 자료형을 포함 [list, tuple, collections.deque]
# Flat : 한 개의 자료형 [str, bytes, bytearray, array.array, memoryview]
# Flat이 더 속도가 빠름 ex. array.array 우선 >> list
# 가변 (Mutable) : list, bytearray, array.array, memoryview, deque
# 불변 (Immutable) : tuple, str, bytes

# 가변/불변 여부, 반복 선택 등에 따른 자료형 선택 필요

import array
import timeit

# 지능형 리스트 (Comprehending Lists)

# Non Comprehending Lists

chars = "!@#$%^^&&!"
codes1 = []

for s in chars:
    codes1.append(ord(s))

# Comprehending List
codes2 = [ord(s) for s in chars]

# Comprehending List + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x: x > 40, map(ord, chars)))

print("EX 1-1 - ", codes1)
print("EX 1-2 - ", codes2)
print("EX 1-3 - ", codes3)
print("EX 1-4 - ", codes4)
print("EX 1-5 - ", [chr(s) for s in codes1])
print("EX 1-6 - ", [chr(s) for s in codes2])
print("EX 1-7 - ", [chr(s) for s in codes3])
print("EX 1-8 - ", [chr(s) for s in codes4])

# Generator

# Generator : 한 번에 한 개의 항목을 생성(Memory 유지 X)
# () 괄호 안에 list comprehension 생성 시 값이 대기 상태로 바뀜
tuple_g = (ord(s) for s in chars)

# Array
array_g = array.array("I", (ord(s) for s in chars))

print("EX 2-1 - ", tuple_g)
print("EX 2-2 - ", next(tuple_g))
print("EX 2-3 - ", next(tuple_g))
print("EX 2-4 - ", array_g)
print("EX 2-5 - ", array_g.tolist())

# Generator sample
print(
    "EX 3-1 - ", ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 11))
)

for s in ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 11)):
    print("EX 3-2 - ", s)

print("\n", "-" * 100, "\n")

# List 주의할 점
marks = [["~"], ["~"], ["~"]], [["~"], ["~"], ["~"]], [["~"], ["~"], ["~"]]
# 복제된 list 3개를 원소로 가지는 list
sample_list = [["~"] * 3]

# 복제된 list 3개를 가지는 list를 복제한 list
# 복제된 list들은 전부 id가 동일함
sample_list_2 = sample_list * 2

print(sample_list, "\n", sample_list_2)
print()
print("복제된 list 2개의 id - ", id(sample_list_2[0]), id(sample_list_2[1]))
print("곱하기 연산자 내의 곱하기 연산자에 의한 메모리 복제 - ", id(sample_list[0][1]), id(sample_list[0][2]))

# 서로 다른 주소의 원소 3개를 각각 선언
# 원소는 복제됐을 때 메모리 주소가 서로 같음을 보여 줌
exlist = [["~"], ["~"], ["~"]]
print("\nlist 내의 메모리를 각각 할당받은 원소 id")
print(id(exlist[0]), id(exlist[1]), id(exlist[2]))

print("\n", "-" * 100, "\n")

# List 주의할 점 >> List Comprehension
# List Comprehension 작성 시 리스트 내에서 마지막 연산/ 명령어 작성을 하는 것이 좋음
marks1 = [["~"] * 3 for o in range(0, 3)]
marks2 = [["~"] * 3] * 3

print("EX 4-3 - ", marks1)
print("EX 4-4 - ", marks2)
print()
print()
print("EX 4-5 - ", [id(i) for i in marks1])
print("EX 4-6 - ", [id(i) for i in marks2])

print()
print()

# Tuple Advanced

# Packing & Unpacking
print("EX 5-1 - ", divmod(100, 9))
print("EX 5-2 - ", divmod(*(100, 9)))  # *tuple >> packing된 상태
print("EX 5-3 - ", *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print("EX 5-4 - ", x, y, rest)
x, y, *rest = range(2)
print("EX 5-5 - ", x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print("EX 5-6 - ", x, y, rest)

print(rest[2])
print("\n", "-" * 100, "\n")


# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print("EX 6-1 - ", l, m, id(l), id(m))


l = l * 2
m = m * 2

print("EX 6-2 - ", l, m, id(l), id(m))

l *= 2
m *= 2

print("EX 6-3 - ", l, m, id(l), id(m))

# 얕은 복사 재할당할 시 tuple은 메모리 재할당

print()


# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ["orange", "strawberry", "mango", "pineapple", "banana", "grape"]

# sorted : 정렬 후 새로운 객체 반환

print("EX 7-1 - ", sorted(f_list))
print("EX 7-2 - ", sorted(f_list, reverse=True))
print("EX 7-3 - ", sorted(f_list, key=len))
print("EX 7-4 - ", sorted(f_list, key=lambda x: x[-1]))
print("EX 7-5 - ", sorted(f_list, key=lambda x: x[-1], reverse=True))


# sort : 정렬 후 객체 직접 변경
# 반환 값 확인 None > 반환 값 없음 > return하지 않는 함수
# 직접 만든 패키지의 함수로 None을 반환하여 return하지 않는 함수라는 것을 상기시켜 줄 필요가 있음

a = f_list.sort()

print("EX 7-6 - ", a, f_list.sort(), f_list)
print("EX 7-7 - ", a, f_list.sort(reverse=True), f_list)
print("EX 7-8 - ", a, f_list.sort(key=len), f_list)
print("EX 7-9 - ", a, f_list.sort(key=lambda x: x[-1]), f_list)
print("EX 7-10 - ", a, f_list.sort(key=lambda x: x[-1], reverse=True), f_list)


# Timeit
# 자료형 속도 비교하기
print("\n", "-" * 100, "\n")

test1 = """
list_ex = [[a, b] for a in ex_1 for b in ex_2]
"""

print(
    timeit.timeit(
        test1,
        setup="""ex_1 = "a b c d".split(" ")
ex_2 = [str(k) for k in range(1, 21)]
""",
        number=100,
    )
)

print()
print()

test2 = """
for a in ex_1:
    list_1st = [a]
    for b in ex_2:
        list_1st = [a, b]
        list_2nd.append(list_1st)
        list_1st = []
"""

print(
    timeit.timeit(
        test2,
        setup="""
ex_1 = "a b c d".split(" ")
ex_2 = [str(k) for k in range(1, 21)]
list_2nd = []
""",
        number=100,
    )
)

print("\n", "-" * 100, "\n")
