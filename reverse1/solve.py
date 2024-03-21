#!/usr/bin/env python3

from itertools import product
from string import ascii_letters, digits
from os import popen

alp = ascii_letters + digits + "_{}"
a = [
    3989823987,
    1684786467,
    1358540119,
    4070158817,
    3333011172,
    847274316,
    154628786,
    2871802435,
    44929898,
    469374164,
    626880303,
    3293050475,
    1524198645,
    3915689234,
]
d = {}

for i in product(alp, repeat=2):
    foo = "".join(i)
    print(foo, end=" ")
    res = int(popen(f"./script.sh '{foo}'").read()[2:], 16)
    print(res)
    d[res] = foo

for i in a:
    print(d[i], end="")
