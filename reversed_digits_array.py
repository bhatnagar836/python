def digitize(n):
    n = str(n)
    new_list = []
    for each_item in n:
        new_list.append(int(each_item))
    # print(new_list)
    new_list.reverse()
    print(new_list)
    return new_list


def solution(string):
    new_s = []
    for item in string:
        new_s.append(item)
        print(new_s)
    new_s.reverse()
    print(''.join(new_s))
    return ''.join(new_s)

# def solution(str):
#   return str[::-1]


solution('world')

digitize(35231)
digitize(0)







