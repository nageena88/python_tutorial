"""for loop , while loop"""

# lst = range(10)
# print(lst)
# lst = list(range(10))  # start,  end, step # 1 argument end_value
# print(lst)
#
# lst = list(range(5, 10))  # 1 argument start_value. 2nd end
# print(lst)
#
# lst = list(range(5, 10, 2))  # 1 argument start_value. 2nd end, 3rd step
# print(lst)

# for x in range(10):
#     print(x, end=" ")

# for x in range(11, 21):
#     print(x, "krishna")


# num = int(input("Enter number for printing table : "))
#
# for x in range(1, 11):
#     print(num * x)

# for x in range(2, 21):
#     for y in range(1, 11):
#         print(f"{x * y:4}", end=" ")
#     print()
# name_caps = "R"
# for x in range(1, 6):
#     for y in range(1, 6):
#         if x == y and x == 3:
#             print(name_caps, end="")
#         else:
#             print("*", end="")
#     print()

# for x in range(1, 6):
#     for y in range(1, x + 1):
#         print("*", end="")
#         # if x == y:
#         #     print("*", end="")
#         # else:
#         #     print(end="")
#     print()


# for x in range(1, 6):
#     for z in range(1, 6 - x):
#         print(" ", end="")
#     for y in range(1, x + 1):
#         print("* ", end="")
#     print()

# for x in range(1, 6):
#     for z in range(1, 6 - x):
#         print(" ", end="")
#     for y in range(1, x + 1):
#         print("* ", end="")
#     print()

# x = "ram" * 3
# print(x)

# for x in range(1, 6):
#     print("*" * x)
#
# for x in range(1, 6):
#     print("{}{}".format(" " * (5 - x), "*" * x))
#
# for x in range(1, 6):
#     print("{}{}".format(" " * (5 - x), "* " * x))

# st = "hello python"
# for x in st:
#     print(x, end=" ")

# lst = [1, 2, 3, 12, 32, 34, 12, 4]
#
# for val in lst:
#     print(val)


# t = (1, 2, 3, 12, 32, 34, 12, 4)
#
# for val in t:
#     print(val)

# s = {1, 2, 3, 12, 32, 34, 12, 4}
#
# for val in s:
#     print(val)

# d = {x: x * x for x in range(1, 5)}
# print(d)
# print(type(d))
#
# for k in d:
#     print(k, d[k])

# for x in {1: 1, 2: 4, 3: 9}:
#     print(x)

# t = 0
# for x in range(1, 1001):
#     t += x
# print(t)

st = input("enter palindrome ")

if st == st[::-1]:
    print(st)
else:
    print("not")
