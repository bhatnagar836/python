def max_len(l1, l2):
    if l1 > l2:
        if 2 * l1 >= l2:
            print(l2)
            return l2
        elif 2 * l1 < l2:
            stick_len = (l2/2)
            print(stick_len)
            return stick_len

    elif l2 > l1:
        if 2 * l2 >= l1:
            print(l1)
            return l1
        elif 2 * l2 < l1:
            stick_len = (l2/2)
            print(stick_len)
            return stick_len
    elif l1 == l2:
        return (l1 + l2)/3

max_len(12,5)