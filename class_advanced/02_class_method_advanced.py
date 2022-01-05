# 02_class_methods_advanced.py
#  객체 지향 프로그래밍(OOP) >>for the Reusage of code, 코드 중복 방지, ..

# Class param, Instance Param

# Class


# General Code

# student 01
class Student():
    """
    Student Class
    Author: Chs
    Date: 20220104
    """
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # Instance Variable
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        # Class Variable (out of method scope)
        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    # Python이 오브젝트 삭제 시 자동으로 delete
    def __del__(self):
        Student.student_count -= 1


# Self 의 의미
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 100, 'score2': 98})
studt2 = Student('Jeong', 4, 1, {'gender': 'Female', 'score1': 100, 'score2': 100}, 'chs991209@naver.com')

# ID 확인
print(id(studt1))
print(id(studt2))

print(studt1._name == studt2._name)
print(studt1 is studt2)

# dir & __dict__ 확인

print(dir(studt1))
print()
print(studt1.__dict__)
print(studt2.__dict__)
#
# email = 선택 매개 변수
#

# Docstring
print(Student.__doc__)
print()

# Method 실행
studt1.detail_info()
studt2.detail_info()

# Student.detail_info()
# self._name, .. 의 인스턴스 할당이 안돼 있음 == self 가 없음

# Class 기반 접근
Student.detail_info(studt1)
Student.detail_info(studt2)

# 비교
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__))

print()

# Instance Variable
# 직접 접근(PEP 권장 X)

print(studt1._name, studt2._name)
print(studt1._email)

# Class variable

# 접근

# Class 내의 어느 위치에서든 접근 가능
print(studt1.student_count)
print(Student.student_count)

print()
print()

# 공유 여부 확인
print(Student.__dict__)
print(studt1.__dict__)
print(studt2.__dict__)

# Instance namespace 에 key, value 가 없으면 Class 에서 검색됨
# Instance 검색 후, Class 에서 검색
# Instance 검색 시 아래에서 위로

del studt2

print(studt1.student_count)

# Student._name >> Class 에서 method만이 할당한 attribute self.param)
