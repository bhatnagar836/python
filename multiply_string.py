def modify_multiply(st, loc, num):
    list_ = st.split()
    word = list_[loc]
    new_list = []
    # print(word)
    for item in range(num):
        new_list.append(word)
    # print("-".join(new_list))
    return "-".join(new_list)


modify_multiply("This is a string",3 ,5)