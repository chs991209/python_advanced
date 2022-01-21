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



