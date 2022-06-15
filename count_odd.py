def odd_count(num):
    if num % 2 == 0:
        num = num -1
        count = int(num / 2) + 1
        print(count)
    else:
        count = int(num/2)
        print(count)
    return count

odd_count(9239062206)