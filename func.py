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


def neighbours(a, b, c):
    p = (a, b, c)
    p1 = ((a + 1) % b, b, c)
    p2 = ((a - 1) % b, b, c)
    p3 = (a, b, (c + 1) % b)
    p4 = (a, b, (c - 1) % b)
    p6 = (a % (b + 1), b + 1, c % (b + 1))
    if b - 1 < 2:
        return (p, p1, p2, p3, p4, p6)
    p5 = (a % (b - 1), b - 1, c % (b - 1))
    return (p, p1, p2, p3, p4, p5, p6)


def calc_K(collection):
    true_p = collection[0]
    all_S = []
    for p in collection[1:]:
        p_delta = oper_p(p, true_p, '-')
        S_val = S(true_p, p_delta)
        if S_val is not None:
            all_S.append(S_val)
    if not all_S:
        return 0
    return max(all_S)


def oper_p(p1, p2, oper):
    if oper == '-':
        a_n = p1[0] - p2[0]
        b_n = p1[1] - p2[1]
        c_n = p1[2] - p2[2]
    if oper == '+':
        a_n = p1[0] + p2[0]
        b_n = p1[1] + p2[1]
        c_n = p1[2] + p2[2]
    return (a_n, b_n, c_n)


def S(p, delta_p):
    Np = count_iter(*p)
    summ = oper_p(p, delta_p, "+")
    Nsumm = count_iter(*summ)

    up_up = abs(Nsumm - Np)
    up_down = max(Np, 1)
    up = up_up / up_down

    all_down = []
    for i in range(len(p)):
        all_down.append(abs(delta_p[i]) /  max(abs(p[i]), 1))
    if max(all_down) == 0:
        return None
    return up / max(all_down)
