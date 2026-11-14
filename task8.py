from func import *

k_stated = 500


def Y(b, k):
    res = set()
    for i in range(k):
        elem = (i * (b - 1)) // (k - 1)
        res.add(elem)
    return sorted(res)


def count_sp_naive(a, b, c):
    res_count = 0
    for y in Y(b, k_stated):
        r_ay_by_b = 1
        for _ in range(y):
            r_ay_by_b = (r_ay_by_b * a) % b
        if r_ay_by_b == c:
            res_count += 1

    return res_count


def count_sp_fastpow(a, b, c):
    res_count = 0
    for y in Y(b, k_stated):
        r_ay_by_b = fast_pow(a, y, b)
        if r_ay_by_b == c:
            res_count += 1

    return res_count


def count_sp_iter(a, b, c):
    res_count = 0
    cur = 1
    Y_b = Y(b, k_stated)
    for y in range(b):
        if y in Y_b:
            if cur == c:
                res_count += 1
        cur = (cur * a) % b

    return res_count


