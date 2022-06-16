def remove_every_other(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i % 2:
            pass
        else:
            new_list.append(my_list[i])
    print(new_list)
    return new_list


remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
remove_every_other(['Hello', 'Goodbye', 'Hello Again'])
remove_every_other([[1, 2]])
remove_every_other([{'Great': 'Job'}, ['Goodbye']])
