def in_asc_order(arr):
    bool_val = True
    for i in range(len(arr)-1):
        current_i = arr[i]
        next_i = arr[i+1]
        if current_i <= next_i:
            pass
        else:
            bool_val = False
    return bool_val
