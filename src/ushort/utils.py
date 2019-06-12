import string
from math import floor


def shorten(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_letters
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res
