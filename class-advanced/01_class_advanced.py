# 01_class_advanced.py
#  객체 지향 프로그래밍(OOP)

# Class param, Instance Param

# Class


# General Code

# student 01
student_name_1 = "Kim"
student_num_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {"gender": "Male"},
    {"score1": 100},
    {"score2": 98},
]

# 코드를 작성하고 실행하면 Python Interpreter 가 주석, 코드를 인식하여
# memory 공간에 params 의 주소와 대입 값을 할당한다.

#  student 02
student_name_2 = "Choi"
student_num_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {"gender": "Female"},
    {"score1": 99},
    {"score2": 97},
]

# student 03
student_name_3 = "Park"
student_num_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {"gender": "Male"},
    {"score1": 98},
    {"score2": 96},
]


# List 구조

# Not proper for administration  관리하기 불편
# Data 의 위치 >> Index 를 매핑해야 함

student_names_list = ["Kim", "Choi", "Park"]
student_numbers_list = [1, 2, 3]
student_grade_list = [1, 2, 4]
student_details_list = [
    {"gender": "Male", "score1": 100, "score2": 98},
    {"gender": "Female", "score1": 99, "score2": 97},
    {"gender": "Male", "score1": 98, "score2": 96},
]

name_list = student_names_list
numbers_list = student_numbers_list
grade_list = student_grade_list
details_list = student_details_list

# Delete a Name

# 원소 직접 삭제는 .remove(원소)  self, value

del name_list[1]
del numbers_list[1]
del grade_list[1]
del details_list[1]

print(name_list)
print(numbers_list)
print(grade_list)
print(details_list)

print()
print()
# Dictionary 구조

students_dicts = [
    {
        "student_name": "Kim",
        "student_number": 1,
        "student_grade": 1,
        "student_detail": {"gender": "Male", "score1": 100, "score2": 98},
    },
    {
        "student_name": "Choi",
        "student_number": 2,
        "student_grade": 2,
        "student_detail": {"gender": "Female", "score1": 99, "score2": 97},
    },
    {
        "student_name": "Park",
        "student_number": 3,
        "student_grade": 4,
        "student_detail": {"gender": "Male", "score1": 98, "score2": 96},
    },
]

del students_dicts[1]
print(students_dicts)
print()
print()
# >>[temp] commit


#  Class 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드


class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    # Override
    def __str__(self):
        return "str : {}, No.{}".format(self._name, self._number)

    def __repr__(self):
        return "repr: {}, No.{}".format(self._name, self._number)


student1 = Student("Kim", 1, 1, {"gender": "Male", "score1": 100, "score2": 98})
student2 = Student("Choi", 2, 2, {"gender": "Female", "score1": 99, "score2": 97})
student3 = Student("Park", 3, 4, {"gender": "Male", "score1": 98, "score2": 96})

# 모든 object 는 namespace 가 dict 기반으로 이루어져 있다.
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# List 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)

# Repeat(__str__)
for x in students_list:
    print(x)
