st = "hello python"
# print(dir(st))
methods = [
    # "capitalize",
    # "casefold",
    # "center",
    # "count",
    # "encode",
    # "endswith",
    # "expandtabs",
    # "find",
    # "format",
    # "format_map",
    # "index",
    # "isalnum",
    # "isalpha",
    # "isascii",
    # "isdecimal",
    # "isdigit",
    # "isidentifier",
    # "islower",
    # "isnumeric",
    # "isprintable",
    # "isspace",
    # "istitle",
    # "isupper",
    # "join",
    # "ljust",
    # "lower",
    # "lstrip",
    "maketrans",
    # "partition",
    # "removeprefix",
    # "removesuffix",
    "replace",
    # "rfind",
    # "rindex",
    # "rjust",
    # "rpartition",
    # "rsplit",
    # "rstrip",
    # "split",
    # "splitlines",
    # "startswith",
    # "strip",
    # "swapcase",
    # "title",
    "translate",
    # "upper",
    # "zfill",
]

# st = "Ram"
# st1 = "ram"
# print(st < st1)
# print(st.__lt__(st1))
# print(len(st))
# print(st.__len__())

# print(st)
# res = st.capitalize()
# print(res)
# print(st)

name = "ram nageena chauhan"
# split_name = name.split()
# print(split_name)
# new_name = [x[0].capitalize() for x in split_name[:-1]]
# print(new_name)
# new_name.append(split_name[-1])
#
# print(new_name)
# sort_name = " ".join(new_name)
# print(sort_name)

# sort_name = (
#     " ".join([x[0].capitalize() for x in name.split()[:-1]]) + " " + name.split()[-1]
# )
# print(sort_name)


# st1 = "Password"
# st2 = "PassWord"
#
# print(st1.casefold() == st2.casefold())

# print(st)
# print(st.center(5))
# print(st.center(50))
# print(st.center(50, "-"))

# print(st.rjust(5))
# print(st.rjust(50))
# print(st.rjust(50, "-"))

# print(st.ljust(5))
# print(st.ljust(50))
# print(st.ljust(50, "-"))


# print(st.count("o"))
# print(st.count("hello python"))
# print(st.count("o", 5))
# print(st.count("o", 5, 9))


# res = st.encode()
# print(res)
#
# print(res.decode())
#
# print(dir(res))

# print(st.startswith("hello"))
# print(st.endswith("on"))

# print(st.find("o"))
# print(st.find("o", 5))
# print(st.find("o", 5, 9))
#
# print(st.find("python"))

# print(st.index("o"))
# print(st.index("o", 5))
# print(st.index("o", 5, 9))

# print(st.index("python"))

# print("abc123".isalnum())
# print("123q".isdecimal())
#
# print(st.islower())
# print(st.isupper())

st1 = "yash"
st2 = "siv"

# res = st1.join(st2)
# print(res)
# print(st1 + st2)

# n = ["Ram", "Chauhan", "abc", "yyasdas"]
#
# st1 = " ".join(n)
# print(st1)

# stu = st.upper()
# print(stu)
# print(stu.lower())
#
# print(stu.title())
# print(st.title())

# print(st.zfill(50))

# print("Yash".swapcase())


# x = st.split()
# print(x)

# x = "ram,shyam,mohan".split(",")
# print(x)

# d = "print(st[6::2])"
# print(d)
# d = d.split("[")[-1]
# d = d.split("]")[0]
# print(d)


# st = """This is a pen.
# this is a another pen."""
#
# print(st.splitlines())

# st1 = "My name is {} and age {}"
#
# name = "Amit"
# age = 30
#
# ss = st1.format(name, age)
# print(ss)

# d = {"name": "Ram", "age": 30, "salary": 2343}
#
# st1 = "My name is {name} and age {age}"
#
# stq = st1.format_map(d)
# print(stq)


# st = "    this is     strip example      "
# print(st)
# print(st.strip())
# print(st.lstrip())
# print(st.rstrip())

# st = "This is cow."

# p = st.partition("is")
# p = st.rpartition("is")
# print(p)


# l = "Total number of sheet = 4032\n"
# l = l.strip()
# l = l.partition("=")
# print(int(l[-1].strip()) + 12)

# st = "This is cow."
# things = "fox"
# st1 = st.replace("cow", things)
#
# print(st1)


# st = "This is cow. cow cow"

# old_val = "cow"
# new_val = "ox"
# print(st.replace(old_val, new_val, 2))

# st = "auto_replace_file"

# print(st.removeprefix("auto_"))
# print(st.removesuffix("_file"))
#
# st = """Since the very beginning,
# we’ve offered a variety of tools and libraries for developers,
# administrators and architects to perform all kind of actions:
# from spinning up Virtual"""
#
# st_1 = "aeiou"
# st_2 = "12345"

# info = str.maketrans(st_1, st_2)

# d = {ord("a"): ord("1")}
# print(info)

# print(ord("a"))

# print(st)
# print("*" * 100)
# new_st = st.translate(d)
# print(new_st)

# for x in range(97, 96 + 27):
#     print(chr(x), end=" => ")
#     print(x, end=" => ")
#     print(chr(x - 32), end=" => ")
#     print(x - 32)
# counter = 0
# for x in range(0, 256):
#     if counter == 10:
#         print()
#         counter = 0
#     print(x, chr(x), end=" ")
#     counter += 1

print(st)

# for s in st:
#     print(s)

# word_list = st.split()
# print(word_list)
# #
# # for x in st.split():
# #     print(x)
# d = list(st)
# d = set(st)
# print(d)
