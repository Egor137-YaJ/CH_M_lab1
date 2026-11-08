tests = [
    (2, 7, 4),
    (2, 7, 3),
    (3, 11, 1),
    (0, 7, 0),
    (0, 7, 1)
]


def count_naive(a, b, c):
    res_count = 0
    for y in range(b):
        r_ay_by_b = 1
        for _ in range(y):
            r_ay_by_b = (r_ay_by_b * a) % b
        if r_ay_by_b == c:
            res_count += 1

    return res_count


def fast_pow(a, y, b):
    if y == 0:
        return 1

    half = fast_pow(a, y // 2, b)
    if y % 2 == 0:
        return (half * half) % b
    else:
        return (half * half * a) % b


def count_fast_pow(a, b, c):
    res_count = 0
    for y in range(b):
        r_ay_by_b = fast_pow(a, y, b)
        if r_ay_by_b == c:
            res_count += 1

    return res_count


def count_iter(a, b, c):
    res_count = 0
    cur = 1
    for y in range(b):
        if cur == c:
            res_count += 1
        cur = (cur * a) % b

    return res_count
