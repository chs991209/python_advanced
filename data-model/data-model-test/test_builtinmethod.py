# String method
"""
String Methods

methods: split(sep=None, maxsplit=-1)
"""

# split Method

# split method 실행
# 문자열만 구분 가능

# sep => string 형태의 구분자(delimiter string => csv doc 에서는 delim 으로도 표현)


split_lit = "a b".split(sep=None, maxsplit=-1)

# 모든 단어 띄어 쓰기 or 엔터로 구분 - Default
# Default split =>  sep, maxsplit 선언 X 가능
# Default maxsplit => 무한으로 delimit

# Seperator string 형태 Error
# "" empty separator -> ValueError:

# Output
print("A B C D E F".split())
print("A B C D E F".split(sep=None, maxsplit=-1))
print("A B C D E F".split(maxsplit=3))
print("a b".split(sep=None, maxsplit=-1))


