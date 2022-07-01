def define_suit(card):
    for character in card:
        if character.isnumeric():
            pass
        else:
            result = {"C": "clubs", "D": "diamonds", "H": "hearts", "S": "spades"}
            if character in result:
                print(result.get(character))
                return result.get(character)


# def define_suit(card):
#     d = {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}
#     return d[card[-1]]

define_suit('9D')