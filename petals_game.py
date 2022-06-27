import itertools


def how_much_i_love_you(nb_petals):
    petals = itertools.cycle(["I love you", "a little", "a lot", "passionately", "madly", "not at all"])
    for i in range(1, nb_petals-1):
        next(petals)

    print(next(petals))
    return next(petals)
    

how_much_i_love_you(4)
# # "I love you")
how_much_i_love_you(334)
# "a lot")
how_much_i_love_you(121)
# "not at all")




# I love you
# a little
# a lot
# passionately
# madly
# not at all
