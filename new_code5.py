def odd_or_even(arr):
    total = 0
    if len(arr)==0:
        return "even"
    else:
        for ele in range(len(arr)):
            total = total + arr[ele]
            
    if total % 2:
        return "odd"
    else:
        return "even"
