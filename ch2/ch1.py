# Operators

# Arithmetics operator
# +, -, /, *, %, //, **

# x, y = 60, 13

# res = x + y
# print(res)

# res = x - y
# print(res)

# res = x / y
# print(res)

# res = x * y
# print(res)

# res = x % y
# print(res)

# res = x // y
# print(res)
# import math
#
# print(math.floor(res))

# res = 2**4
# print(res)

# Relational operator
# >, >=, <, <=, ==, !=


# res = x > y
# print(res)
#
# res = x >= y
# print(res)
#
# res = x < y
# print(res)
#
# res = x <= y
# print(res)
#
# res = x == y
# print(res)

# res = x != y
# print(res)

#
# res = ["Ram"] == ["Ram"]
# print(res)

# Logical operator
# and, or, not(&&, ||, !)

# res = False and False
# print(res)
#
# res = False and True
# print(res)
#
# res = True and False
# print(res)
#
# res = True and True
# print(res)

# res = False or False
# print(res)
#
# res = False or True
# print(res)
#
# res = True or False
# print(res)
#
# res = True or True
# print(res)

# res = not False
# print(res)
#
# res = not True
# print(res)

# a, b, c = 1020, 300, 40
#
# if a > b and a > c:
#     res = a
# elif b > c:
#     res = b
# else:
#     res = c
#
# print(res)

# ch = "A"
# ch = ch.upper()

# if ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
#     print("vowel")
# else:
#     print("Consonant")

# x = 13
# if not x % 2:
#     print("even")
# else:
#     print("odd")

# a = 898
#
# print(bool(a))

# Assignment operator
# a = 12
# res = x + y
# x = x + y
# x += y
# x += y
# x = x + y
# print(x)
# print(y)
# == and = kya differences

# membership operator
# in, not in
# st = "I am a c++ trainer."
# print("java trainer" in st)

# lst = {2, 3, 12, 4, 65, 3, 412, 145, 6, 13}
#
# print(x in lst)
# print(y in lst)

# if "java" in st:
#     st = st.replace("java", "python")
# print(st)

# print("java" not in st)

# identity operator
# is , is not

# z = 60

# st = "Hello"
# st1 = "Hello"
# print(st)
# print(st1)
# print(id(st))
# print(id(st1))
# print(st is st1)
# print(st == st1)

# st1 = "H" + st[1:]
# print(st)
# print(st1)
# print(id(st))
# print(id(st1))
# print(st is st1)
# print(st == st1)
# print(st[1:])
# print(st is not st1)

# bitwise operator
# &, |, ~, ^, <<, >>

x, y = 60, 13
# print(f"{x} and {y}")
# print("{} and {}".format(x, y))

print(f"x     : {x:08b}")
# print(f"y     : {y:08b}")
# print(f"x & y : {x & y:08b}")
# print(f"x | y : {x | y:08b}")
# print(f"x ^ y : {x ^ y:08b}")
#
# print(x & y)
# print(x | y)
# print(x ^ y)

# print(~x)

print(x << 2)
z = x >> 3
print(z)
print(z << 2)
