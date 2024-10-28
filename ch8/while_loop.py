"""while loops"""

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print(i)


# x = 1
# while x <= 5:
#     y = 1
#     while y <= x:
#         print("*", end="")
#         y += 1
#     x += 1
#     print()
#
# for x in range(1, 6):
#     for y in range(1, x + 1):
#         print("*", end="")
#     print()


# counter = 0
# while True:
#     counter += 1
#     print("Hello")
#     if counter == 10:
#         break

# pass_word = "Password_1"
#
# counter = 3
#
# while True:
#     p = input("enter your Password : ")
#     counter -= 1
#     if pass_word == p:
#         print("Login success!")
#         break
#     elif counter == 0:
#         print("max retry done")
#         print("please try after some time")
#         print("With correct credential")
#         exit(0)
#     else:
#         print("your password is wrong ")
#         print("try again !")
#
# print("welcome back")


# lst = [12, 234, 23, 223, 12, 14, 4, 1, 5, 2356, 577]
#
# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1

#
# d = {"name": "Ram", "age": 36, "add": "Pune"}
# lst = list(d.keys())
#
# i = 0
# while i < len(lst):
#     print(lst[i], d[lst[i]])
#     i += 1

# counter = 1
# for x in range(1, 6):
#     for y in range(1, 6 - x):
#         print(" ", end="")
#     for z in range(counter):
#         print("*", end="")
#     counter += 2
#     print()
#
# counter -= 4
# for x in range(1, 5):
#     for y in range(x):
#         print(" ", end="")
#     for z in range(counter):
#         print("*", end="")
#     counter -= 2
#     print()

# counter = 1
# for x in range(1, 6):
#     for y in range(1, 6 - x):
#         print(" ", end="")
#     for z in range(counter):
#         print("*", end="")
#     counter += 1
#     print()
#
# counter -= 2
# for x in range(1, 5):
#     for y in range(x):
#         print(" ", end="")
#     for z in range(counter):
#         print("*", end="")
#     counter -= 1
#     print()
