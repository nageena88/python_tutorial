st = "hello python"
# print(dir(st))
methods = [
    # "capitalize",
    # "casefold",
    # "center",
    # "count",
    # "encode",
    # "endswith",
    "expandtabs",
    # "find",
    "format",
    "format_map",
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
    "lstrip",
    "maketrans",
    "partition",
    "removeprefix",
    "removesuffix",
    "replace",
    # "rfind",
    # "rindex",
    # "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "split",
    "splitlines",
    # "startswith",
    "strip",
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

print(st)
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

d = "print(st[6::2])"
print(d)
d = d.split("[")[-1]
d = d.split("]")[0]
print(d)
