# kata7
import math

def gps(s, x):
    new_list = []
    for i in range(len(x) - 1):
        current_item = x[i]
        next_item = x[i + 1]
        new_list.append((3600 * (next_item - current_item)) / s)
    print(new_list)
    max_avg_speed = math.floor(max(new_list, default=0))
    # default function added because of "MAX () arg is an empty sequence in Python" error
    print(max_avg_speed)
    return max_avg_speed



    #     item = (3600 * items) / s
    #     new_list.append(items)
    # print(new_list)


# gps(20, [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61])
gps(15,  [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25])
# gps(12, [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25])