import random
import time
import math

# f = random.random()
# print(f)

# random_val = []
# for x in range(10):
#     random_val.append(round(random.random(), 3))

# print(dir(math))
# print(random_val)
#
# print(dir(random))

methods = [
    "choice",
    "choices",
    "gauss",
    "randint",
    "random",
    "randrange",
    "sample",
    "seed",
    "shuffle",
    "triangular",
    "uniform",
]

lst = [2, 4, 5, 7, 89]

# print(random.choice(lst))
# print(random.choices(lst, k=2))

# print(random.gauss(10, 0.5))

# print(random.randint(3, 7))

# print(list(range(1, 50)))

# print(random.randrange(1, 50))

# lst.clear()
# for x in range(50):
#     lst.append(random.randrange(1, 50))
#
# print(lst)
# # lst = list(range(1, 51))
# print(random.sample(lst, k=10))

lst.clear()
# print(lst)
lst.extend([x for x in range(1, 100)])
# print(lst)

# while True:
#     if len(lst) == 0:
#         print("Game is Done")
#         exit(0)
#     else:
#         rand_val = random.choice(lst)
#         lst.remove(rand_val)
#         print(f"next value is {rand_val}")
#         time.sleep(2)

# random.seed(120)
#
# while len(lst) > 0:
#     rand_val = random.choice(lst)
#     lst.remove(rand_val)
#     print(f"next value is {rand_val}")
#     # time.sleep(2)
#
# print("Game is Done")

# print(lst)
#
# random.shuffle(lst)
#
# print(lst)
print(random.uniform(4.5, 12.7))
