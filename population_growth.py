# kata7
import math


def nb_year(p0, percent, aug, p):
    num_of_years = 0
    while p0 < p:
        p0 = math.floor(p0 + (p0 * (percent/100)) + aug)
        num_of_years += 1
    print(num_of_years)
    return num_of_years


nb_year(1000, 2, 50, 1200)
nb_year(1500, 5, 100, 5000)