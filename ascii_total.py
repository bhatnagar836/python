def uni_total(s):
    total = 0
    if s == "":
        print(0)
        return 0
    else:
        for items in s:
            asc_value = ord(items)
            # print(asc_value)
            total = total + asc_value
        print(total)
        return total
    
# def uni_total(s):
#     return sum(ord(c) for c in s)


uni_total("")
uni_total("Mary Had A Little Lamb")
