import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "<>,.?/:!@#$%^&*()_+={}[]"

upper, lower, nums, symbl = True, True, False, False

all = ""

if upper:
    all += upper_case
if lower:
    all += lower_case
if nums:
    all += digits
if symbl:
    all += symbols

length = 10
lines = 1

for x in range(lines):
    password = "".join(random.sample(all, length))
    print(password)
