from func import count_iter as N

a_tests = [2, 3, 5]
b_tests = [7, 11, 13, 17]

a_jumps, b_jumps, c_jumps = [], [], []

for a in a_tests:
    for b in b_tests:
        for c in range(b):
            c_1 = (c + 1) % b
            n = N(a, b, c)
            n1 = N(a, b, c_1)
            if abs(n1 - n) >= 2:
                c_jumps.append(((a, b, c), (a, b, c_1), n, n1))

for a in a_tests:
    for b in b_tests:
        for c in range(b):
            a1 = a + 1
            a2 = a - 1
            n = N(a, b, c)
            n1 = N(a1, b, c)
            n2 = N(a2, b, c)
            if abs(n1 - n) >= 2:
                a_jumps.append(((a, b, c), (a1, b, c), n, n1))
            if abs(n2 - n) >= 2:
                a_jumps.append(((a, b, c), (a2, b, c), n, n2))

for a in a_tests:
    for b in b_tests:
        for c in range(b):
            b1 = b + 1
            b2 = b - 1
            n = N(a, b, c)
            n1 = N(a, b1, c)
            n2 = N(a, b2, c % b2)
            if abs(n1 - n) >= 2:
                b_jumps.append(((a, b, c), (a, b1, c), n, n1))
            if abs(n2 - n) >= 2:
                b_jumps.append(((a, b, c), (a, b2, c % b2), n, n2))

print(a_jumps)
print(b_jumps)
print(c_jumps)





