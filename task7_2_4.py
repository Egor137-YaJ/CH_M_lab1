from task7_2_3 import *


for row in test_points:
    p = row[0]
    Np = count_iter(*p)
    if Np == 0:
        for neigh_p in row[1:]:
            delta_p = oper_p(neigh_p, p, '-')
            Np_neigh = count_iter(*neigh_p)
            s = S(p, delta_p)
            if Np_neigh > 0:
                print(p, '\t', neigh_p, '\t', Np, '\t', Np_neigh, '\t', s)
