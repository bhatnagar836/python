def find_short(s):
    counter = []
    x = s.split()
    print(x)
    for items in x:
        counter.append(len(items))
    min_ele = min(counter)
    # print(min_ele
    return min_ele



find_short("Let's travel abroad shall we")