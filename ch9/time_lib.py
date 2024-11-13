import time

# print(dir(time))

methods = [
    "altzone",
    "asctime",
    "ctime",
    "gmtime",
    "localtime",
    "mktime",
    "process_time",
    "sleep",
    "strftime",
    "strptime",
    "struct_time",
    "time",
    "time_ns",
    "timezone",
    "tzname",
]
# print(time.time())
#
# print(time.altzone)
#
# print(time.asctime())
# print(time.localtime(200))

# print(time.asctime(time.localtime(10)))

# x = time.mktime((1980, 12, 1, 3, 45, 10, 0, 0, 0))
# print(x)

# print(time.asctime(time.localtime(x)))
# print(time.ctime())
# t = time.time()
# time.sleep(1)
# for x in range(10):
#     print(x)
#     # time.sleep(1)
# t1 = time.time()
# print("Process time", t1 - t)
# # print(time.process_time())

# print(time.tzname)
# print(time.timezone)

st = time.strftime("%Y-%m-%d_%H%M%S", time.localtime(time.time()))
f_name = "ram_test"
file_name = f_name + st + ".txt"

# from pathlib import Path
#
# p = Path(".").absolute()
# file_path = p.joinpath(file_name)
# file_path.touch()

import calendar

print(calendar.month(2024, 2))
print(calendar.isleap(2024))
print(calendar.leapdays(1990, 2024))
print(calendar.calendar(2024))

print(calendar.MONDAY)

from datetime import datetime

print(dir(datetime))

print(datetime.now().minute)
