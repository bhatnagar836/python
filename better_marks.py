def better_than_average(class_points, your_points):
    sum = 0
    count = len(class_points)
    for elements in class_points:
        sum = sum + elements
    # print(count)
    avg = sum/count
    print(True) if avg < your_points else print(False)
    return True if avg < your_points else False



better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)