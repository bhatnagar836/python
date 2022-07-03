def points(games):
    sum = 0
    for elements in games:
        if elements[0] > elements[2]:
            sum += 3
        elif elements[0] < elements[2]:
            sum += 0
        elif elements[0] == elements[2]:
            sum += 1
    print(sum)
    return sum


points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])
