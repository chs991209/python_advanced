from collections import namedtuple


class StudentCode(object):
    @staticmethod
    def findalpha_namedtuple(passed_list):
        """
        Author : Chs
        Date : 20220106
        :param passed_list:
        :return: studtsnum_namedtuple_list
        """
        num_A = 0
        num_B = 0
        num_C = 0
        num_D = 0
        num_E = 0
        num_F = 0
        num_G = 0
        num_H = 0
        Passednum_namedtuple = namedtuple("Passed_studts_num", "cls_alpha, num")

        #
        for a in passed_list:
            if "a" in a:
                num_A += 1
            if "b" in a:
                num_B += 1
            if "c" in a:
                num_C += 1
            if "d" in a:
                num_D += 1
            if "e" in a:
                num_E += 1
            if "f" in a:
                num_F += 1
            if "g" in a:
                num_G += 1
            if "h" in a:
                num_H += 1
            else:
                pass
        clsA = Passednum_namedtuple("A", num_A)
        clsB = Passednum_namedtuple("B", num_B)
        clsC = Passednum_namedtuple("C", num_C)
        clsD = Passednum_namedtuple("D", num_D)
        clsE = Passednum_namedtuple("E", num_E)
        clsF = Passednum_namedtuple("F", num_F)
        clsG = Passednum_namedtuple("G", num_G)
        clsH = Passednum_namedtuple("H", num_H)

        studtsnum_namedtuple_list = [clsA, clsB, clsC, clsD, clsE, clsF, clsG, clsH]

        return studtsnum_namedtuple_list

    @staticmethod
    def findalpha(passed_list):
        """
        Counts the number of the elements of the student codes' list which contains each alphabet from a to z.
        Each alphabet is the key of the returned dictionary and the value of each alphabet is the counted number of
        the student-elements of the list which contain each alphabet.
        Each student code contains the alphabet of each student's class name, and the class names are from A to Z.
        Author : Chs
        Date : 20220106
        :param passed_list: type=class, list
        :return:passed_studts_distributed_dict: type=class, A: 1, B: 2, ..
        """

        numof_A = 0
        numof_B = 0
        numof_C = 0
        numof_D = 0
        numof_E = 0
        numof_F = 0
        numof_G = 0
        numof_H = 0

        for a in passed_list:
            if "a" in a:
                numof_A += 1
            if "b" in a:
                numof_B += 1
            if "c" in a:
                numof_C += 1
            if "d" in a:
                numof_D += 1
            if "e" in a:
                numof_E += 1
            if "f" in a:
                numof_F += 1
            if "g" in a:
                numof_G += 1
            if "h" in a:
                numof_H += 1
            else:
                pass

        # classnamealpha_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        # class_l = classnamealpha_list
        # passed_studts_num_list = [
        #     numof_A,
        #     numof_B,
        #     numof_C,
        #     numof_D,
        #     numof_E,
        #     numof_F,
        #     numof_G,
        #     numof_H,
        # ]
        # passed_num_l = passed_studts_num_list

        # passed_studts_num_listpassed_studts_alpha_distributed = {}
        # for z in range(len(class_l)):
        #     passed_studts_alpha_distributed[class_l[z]] = passed_num_l[z]
        #
        # return passed_studts_alpha_distributed
        passed_studts_distributed_dict = {
            "A": numof_A,
            "B": numof_B,
            "C": numof_C,
            "D": numof_D,
            "E": numof_E,
            "F": numof_F,
            "G": numof_G,
            "H": numof_H,
        }

        return passed_studts_distributed_dict

    @staticmethod
    def findalnum(passed_list):
        studts_alnum_list = []
        for k in passed_list:
            for j in k:
                if j.isalnum():
                    studts_alnum_list.append(j)


# Class 에 던질 object 생성
list_test = ["a2", "b3", "c2", "h2"]

print("\n" + str("-" * 100) + "\n")
print("findalpha :", StudentCode.findalpha(list_test))
#
print("\n" + str("-" * 100) + "\n")
#

# 반환 값 출력
test_namedtuplelist = StudentCode.findalpha_namedtuple(list_test)
print("Return 된 값 출력 : {}\n".format(test_namedtuplelist))
print("Return 된 값 repr: {}\n".format(repr(test_namedtuplelist)))
# 반환 값 정보
print('__dir__ : {}'.format(test_namedtuplelist.__dir__()))

# index 호출 (Namedtuple)
print(test_namedtuplelist[0])
print()

# Class 접근 방식
print(test_namedtuplelist[0].cls_alpha)

#
print("\n" + str("-" * 100) + "\n")
#


# Dictionary 형 -> 하나의 Dict 으로 변환 (Namedtuple)
dict_Test = dict((a.cls_alpha, a.num) for a in test_namedtuplelist)

# Output
print(dict_Test)

# Dict 으로 변환하면 key 값으로 호출

