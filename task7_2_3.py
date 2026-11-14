from func import *

test_points = [(3, 13, 1), (3, 13, 0),
               (2, 7, 4), (2, 7, 3),
               (3, 17, 9), (2, 17, 0),
               (5, 13, 8), (2, 11, 5),
               (0, 7, 0), (1, 7, 1)]


for i in range(len(test_points)):
    cur_point = test_points[i]
    test_points[i] = neighbours(*cur_point)


for row in test_points:
    print(row[0], '\t', count_iter(*row[0]), '\t', calc_K(row))




