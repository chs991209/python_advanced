# Class Method, Instance method, Static method

# Instance Method


class Student(object):
    """
    Student Class
    Author : Chs
    Date : 20220105
    Description : Class, Static, Instance Method
    """

    # 등록금 인상률
    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # (self) >> instance method
    # 외부의 param 들에서 args를 받아 할당함
    def full_name(self):
        return "{} {}".format(
            self._first_name, self._last_name
        )

    # Instance method
    def detail_info(self):
        return "Student Detail Info : {}, {} {}, {}, {}, {}, {}".format(
            self._id,
            self._first_name,
            self._last_name,
            self._email,
            self._grade,
            self._tuition,
            self._gpa,
        )

    # Instance Method
    def get_fee(self):
        return "Before Tuition Increase -> Id : {}, fee : {} $".format(
            self._id, self._tuition
        )

    # Instance Method
    def get_fee_culc(self):
        return "After Tuition Increase -> Id : {}, fee : {} $".format(
            self._id, self._tuition * Student.tuition_per
        )

    # Important
    def __str__(self):
        return "Student Info -> name : {} grade : {} email : {}".format(
            self.full_name(), self._grade, self._email
        )

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print("Please Enter ratio more than 1")
            return

        # else >> per > 1
        cls.tuition_per = per
        print("Done! Tuition has increased")

    # Class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(
            id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa
        )

    # Static Method
    @staticmethod
    def is_scholarship(studt):
        if studt._gpa >= 4.3:
            return "{} is a scholarship Recipient.".format(studt._last_name)
        return "Not a scholarship Recipient."

    @staticmethod
    def is_plural_scholarship(studts_list):
        # yes_scholarship_list = []
        # no_scholarship_list = []
        yes_scholarship_namestring = ""
        no_scholarship_namestring = ""
        try:
            for a in studts_list:
                if a._gpa >= 4.3:
                    # yes_scholarship_list.append(a._last_name)
                    yes_scholarship_namestring += str(a._last_name) + ", "

                # no_scholarship_list.append(a._last_name)
                no_scholarship_namestring += str(a._last_name) + ", "
            # return '{} is a scholarship recipient'.format(yes_scholarship_list[len(yes_scholarship_list)])
            return "O : {} is/are scholarship recipients".format(
                yes_scholarship_namestring
            ) + "\n\nX : {} is/are not scholarship recipient".format(
                no_scholarship_namestring
            )
        except TypeError:
            return (
                ">>>>>>>TypeError occurred: Please check the gpa of the studtslist's parameters"
                "Implement method Student.type_gpa(studts_list), print() and run if you want to check )"
            )

    @staticmethod
    def type_gpa(studts_list):
        gpa_string = ""
        for i in range(len(list)):
            gpa_string += (
                "\n"
                + str("-" * 100)
                + "\nStudent {} 's Gpa is : {}".format(
                    studts_list[i].__dict__["_last_name"],
                    studts_list[i].__dict__["_gpa"],
                )
            )

        return gpa_string


# Student Instance
student_1 = Student(3, "Sojeong", "Lee", "sojeonglee@gmail.com", "3", 2000, 4.1)
student_2 = Student(4, "William", "Shakespear", "shakespear@gmail.com", "4", 3000, 4.3)

# Basic Info (__str__)
print(student_1)
print()


# General Info
print(student_1.detail_info())
print(student_2.detail_info())
print(Student.detail_info.__dir__())

# Fee Info(Before Increase)
print(student_1.get_fee())
print(student_2.get_fee())

print()

# 직접 접근-비추천
Student.tuition_per = 1.2  # Class instance

# Class Method @classmethod
Student.raise_fee(1)
Student.raise_fee(1.3)

# Fee Info(After Increase)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()

# Class method Instance Construction
student_3 = Student.student_const(
    3, "Sujeong", "Jeong", "krystal@gmail.com", "3", 3000, 4.4
)
student_4 = Student.student_const(
    4, "Chaejun", "Park", "chaejunpark@gmail.com", "3", 2800, 4.4
)

# General Info
print(student_3.detail_info())
print(student_3.get_fee_culc())
print(student_3._tuition)

# 장학금 여부(static method X)


# 장학금 여부(static method)
print(Student.is_scholarship(student_4))
print()
# 장학금 여부 string output static method
list = [student_1, student_2, student_3, student_4]
print(Student.is_plural_scholarship(list))
print(Student.type_gpa(list))
