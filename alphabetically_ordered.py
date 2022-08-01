def alphabetic(s):
    bool_val = True
    new_list = []
    for i in range(len(s)):
        current_item = ord(s[i])
        new_list.append(current_item)
    # print(new_list)
    for i in range(len(new_list)-1):
        current_item = new_list[i]
        next_item = new_list[i+1]
        if current_item > next_item:
            bool_val = False
        else:
            pass
    return True if bool_val else False



alphabetic("ant")