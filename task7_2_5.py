from func import count_iter as N
from func import neighbours, calc_K, S, oper_p
import matplotlib.pyplot as plt


k_N0 = 0
k_Nmore2 = 0
point_max_K = []
point_S0 = 0

all_N = []
b_list = []
share_list = []

for b in range(50, 1, -1):
    count_changed_points_this_b = 0
    for a in range(b):
        for c in range(b):
            p = (a, b, c)
            Np = N(*p)
            all_N.append(Np)
            p_neighs = neighbours(*p)
            K_p = calc_K(p_neighs)

            if Np == 0:
                k_N0 += 1
            elif Np >= 2:
                k_Nmore2 += 1
            point_max_K.append((K_p, p))
            if all(S(p, oper_p(p_neigh, p, '-')) == 0 for p_neigh in p_neighs[1:]):
                point_S0 = p
                count_changed_points_this_b += 1
    b_list.append(b)
    share_list.append(count_changed_points_this_b / (b * b))

point_max_K.sort(key=lambda x: x[0])
print(k_N0, k_Nmore2, point_max_K[-1][1], point_S0)


import matplotlib.pyplot as plt

plt.hist(all_N, bins=range(0, max(all_N) + 2), align="left")
plt.yscale("log")
plt.xlabel("N(a, b, c)")
plt.ylabel("число точек")
plt.title("Распределение N при b ≤ 50")
plt.grid(True)
plt.savefig("hist_N.png")
plt.show()

plt.plot(b_list, share_list, marker="o")
plt.xlabel("b")
plt.ylabel("доля точек с ΔN ≠ 0")
plt.title("Доля чувствительных точек в зависимости от b")
plt.grid(True)
plt.savefig("share_dN.png")
plt.show()
