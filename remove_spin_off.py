# kata8

def array(string):
    if len(string) <= 3 or not string:
        print(None)
        return None
    # elif len(string)
    else:
        new_list = []
        x = string.split(",")
        # print(x)
        for items in x[1:len(x) - 1]:
            new_list.append(items)
        y = " ".join(new_list)
        print(y)
        if y == '':
            return None
        return str(y)


array('1,2,3,4')
array('1, ,2')
array('1,2,3,4,5')
array("")