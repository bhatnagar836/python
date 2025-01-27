def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(0,3):
        if a[i]>b[i]:
            alice = alice +1
        elif a[i]<b[i]:
            bob = bob + 1
        else:
            alice = alice + 0
            bob = bob + 0
        arr = [alice,bob]
    print(arr)
        # return arr

compareTriplets([1, 2, 3], [3, 2, 1])