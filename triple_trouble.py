def triple_trouble(one, two, three):
    if len(one) == len(two) and len(two) == len(three):
        new_str = ""
        for index_i in range(len(one)):
            new_str += one[index_i] + two[index_i] + three[index_i]
        print(new_str)
        return new_str


triple_trouble("aa", "bb", "cc")
