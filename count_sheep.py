def count_sheep(n):
    count = 0
    words = ""
    while count < n:
        count += 1
        words = words + str(count) + " sheep..."
    print(words)
    return words




count_sheep(3)