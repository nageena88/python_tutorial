"""set"""

# A = set()
# A = {1, 2}
# A = set([1, 2])
# print(type(A))
# print(A)

# a = {1, 2, 3, 4, 5, 2, 1, 3}
# print(a)
# l = [1, 2, 3, 4, 5, 2, 1, 3]
#
# print(type(l))
# print(l)
# a = set(l)
#
# print(a)
#
# print(a[0])

a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}

# print(a)
# print(b)

# print(a - b)
# print(b - a)

# print(a + b)  # not possible

# print(dir(a))

methods = [
    "add",
    "clear",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "isdisjoint",
    "issubset",
    "issuperset",
    "pop",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
]

# a.add(99)
# a.add(99)
# a.add(99)
# a.add(99)
#
# print(a)

# diff = a.difference(b)
# diff = b.difference(a)
# print(diff)
# print(a)
# print(b)

# a.difference_update(b)
# b.difference_update(a)
# a = a - b
# b = b - a
# print(a)
# print(b)

# inter_sect = a.intersection(b)
# print(inter_sect)
# sym_diff = a.symmetric_difference(b)
# print(sym_diff)


# x = a.union(b)
# print(a)
# print(b)
# print(x)

# a.update(b)
# print(a)
#
# print(b)

print(a)
# a.discard(6)
# a.discard(60)
# print(a)

# a.remove(6)
# a.remove(60)
# print(a)

# x = a.pop()
# print(x)
# print(a)

# print(a.isdisjoint(b))
# x = {1, 2, 3}
# y = {6, 7, 8}
# print(x.isdisjoint(y))
# print(x.issubset(y))
# print(x.issuperset(y))

# x = {1, 2, 3, 4, 5, 6}
# y = {4, 5, 6}
# print(x.issubset(y))
# print(x.issuperset(y))
#
# print(y.issubset(x))
# print(y.issuperset(x))

l = list(range(1, 101))
# print(l)
# for x in a:
#     print(x)

d = set()
for x in l:
    if x % 5 == 0:
        d.add(x)
    else:
        print("skip...")
    print("processing....")

print("Processing are Done!")
print(d)
