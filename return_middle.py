def get_middle(s):
    return s[int(len(s)/2)] if len(s) % 2 else s[int(len(s)/2)-1:int(len(s)/2)+1]

get_middle("test")
# "es"
get_middle("testing")
# "t"
get_middle("middle")
# "dd"
get_middle("A")
# "A"
get_middle("of")
# "of"