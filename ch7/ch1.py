"""decision-making"""

# if
# if else
# ladder if else
# nested if else

even = []
odd = []
# for x in range(1, 11):
#     if x % 2:
#         odd.append(x)
#     # else:
#     #     even.append(x)
# #
# print(even)
# print(odd)

# x = -5
# if x < 0:
#     print(x)
#     print("-ve")
# else:
#     print(x)
#     print("+ve")

# x = 1
# if x:
#     print("Hello")
# else:
#     print("Hi")


# for x in range(1, 11):
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
#
# print(even)
# print(odd)

# total_marks = int(input("Enter total marks : "))
# result = None
# if total_marks < 0:
#     print("you put marks are wrong!")
#     exit(0)
# if total_marks <= 40:
#     result = "Fail"
# elif total_marks <= 50:
#     result = "D Grade"
# elif total_marks <= 60:
#     result = "C Grade"
# elif total_marks <= 70:
#     result = "B Grade"
# elif total_marks <= 80:
#     result = "B+ Grade"
# elif total_marks <= 90:
#     result = "A Grade"
# elif total_marks <= 100:
#     result = "A+ Grade"
# else:
#     print("you put marks are wrong!")
#     result = 0
#
# print(result)

x, y, z = 120, 34, 500

# ladder
if x > y and x > z:
    print(x)
elif y > z:
    print(y)
else:
    print(z)

# nested

if x > y:
    if x > z:
        print(x)
    else:
        print(z)
elif y > z:
    print(y)
else:
    print(z)
