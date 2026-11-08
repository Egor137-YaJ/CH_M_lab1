import time, matplotlib.pyplot as plt
from func import *


def measure(func, a, b, c):
    start = time.perf_counter()
    func(a, b, c)
    end = time.perf_counter()
    return end - start

b_measures = [100, 300, 1000, 3000, 10000]
naive_measures = []
fastpow_measures = []
iter_measures = []

for b in b_measures:
    naive_measures.append(measure(count_naive, 2, b, 1))
print(naive_measures)

for b in b_measures:
    fastpow_measures.append(measure(count_fast_pow, 2, b, 1))
print(fastpow_measures)

for b in b_measures:
    iter_measures.append(measure(count_iter, 2, b, 1))
print(iter_measures)


plt.loglog(b_measures, naive_measures, marker="o", label="naive")
plt.loglog(b_measures, fastpow_measures, marker="o", label="fastpow")
plt.loglog(b_measures, iter_measures, marker="o", label="iter")

plt.xlabel("b")
plt.ylabel("время, с")
plt.title("Время подсчёта N(2, b, 1), полный диапазон y")
plt.legend()
plt.grid(True, which="both")
plt.savefig("time_full.png")
plt.show()
