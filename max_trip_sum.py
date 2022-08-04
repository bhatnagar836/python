def max_tri_sum(numbers):
    x = list(set(numbers))
    x.sort(reverse= True)
    return sum(x[0:3])


max_tri_sum([2,1,8,0,6,4,8,6,2,4])