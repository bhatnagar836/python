# kata 7
def tidyNumber(n):
    counter = len(str(n))
    arr = []
    while counter:
        modu = n % 10
        n = int((n - modu)/10)
        counter -= 1
        arr.append(modu)
    print(arr)

    bool_val = True
    for i in range(len(arr)-1):
        current_item = arr[i]
        next_item = arr[i+1]
        if current_item < next_item:
            bool_val = False

    return True if bool_val else False


tidyNumber(9672)
tidyNumber(27789)