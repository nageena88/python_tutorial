"""dict"""

import json

d = {"name": "Ram", "age": 34, "course": "Python"}

# d = dict(name="Ram", age=34, course="Python")
# print(type(d))
# print(d)


# print(d["name"])
# # print(d["age"])
#
# d["name"] = "Ravi"
# d["salary"] = 234242

print(d)

# records = [["Ram", "Pune", 234354354, "python"], ["Mumbai", "amit", 345356, "java"]]
# print(records[1][0])
# records = [
#     dict(name="Ram", add="Pune", phone=234354354, course="python"),
#     dict(add="Mumbai", name="amit", phone=345356, course="java"),
# ]
# print(records[0]["add"])

# del d["course"]

# print(d)

# print(d["salary"])

# print(dir(d))

methods = [
    "clear",
    "copy",
    "fromkeys",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
]

# ls = ["name", "age", "add", "phone"]

# student = dict.fromkeys(ls, "NA")
# print(student)

# student = {}
# for x in ls:
#     msg = "Enter {} : ".format(x)
#     value = input(msg)
#     student[x] = value
#
# print(student)


# val = d.get("name")
# if val is not None:
#     print(val)
# else:
#     print("key does not exist")

# print(d.items())
# for key, val in d.items():
#     # if val == "Ram":
#     #     print(key)
#     print(key, "=>", val)

# for x in d.items():
# key, val = x
# print(key, val)
# print(x[0], x[1])

# print(d.keys())

# for key in d.keys():
#     print(key, d[key])

# print(d.values())

# for val in d.values():
#     print(val)

# x = d.setdefault("name", "Ajay")
# x = d.get("name", "Ajay")

# x = d.setdefault("salary", 23000)
# x = d.get("salary", 23000)

# print(x)
# print(d)

# x = d.pop("name")
# x = d.pop("salary")
# x = d.pop()

# print(x)
# print(d)

# info = d.popitem()
# print(info)
# print(d)

# d1 = {"name": "Aamitya", "age": 30, "salary": 233323}
# print(d1)
#
# d.update(d1)
# print("-" * 40)
# print(d)
# print(d1)
#
# students = {
#     "1": {
#         "1": {"name": "Ram"},
#         "2": {"name": "ajay"},
#         "3": {"name": "priya"},
#     },
#     "2": {
#         "1": {"name": "amit"},
#         "2": {"name": "suresh"},
#         "3": {"name": "anjali"},
#     },
#     "3": {
#         "1": {"name": "anamika"},
#         "2": {"name": "advika", "marks": [12, 3, 2, 12, 4, 1]},
#         "3": {"name": "ayush", "marks": None},
#     },
# }

# print(students["3"]["2"])

data = json.dumps(students, indent=4)
# f = open("abc.json", "w")
# f.write(data)
# f.close()
