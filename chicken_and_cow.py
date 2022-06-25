def animals(heads, legs):
    my_tuple = []
    if heads > 0 and legs > 0:
        cows = (legs - (heads * 2))/2
        chickens = heads - cows
        # print("Number of chickens = ", chickens, "and cows = ", cows)
        if cows-int(cows) == 0 and chickens-int(chickens) == 0 and cows >= 0 and chickens >= 0:
                my_tuple.append(int(chickens))
                my_tuple.append(int(cows))
                # print(tuple(my_tuple))
                return tuple(my_tuple)
        else:
            # print("No solutions")
            return "No solutions"
    elif heads < 0 or legs < 0:
        print("No solutions")
        return "No solutions"
    elif heads == 0 and legs == 0:
        return 0, 0
    elif heads == 0 or legs == 0:
        # print("No solutions")
        return "No solutions"



animals(54, 956)
# "No solutions"