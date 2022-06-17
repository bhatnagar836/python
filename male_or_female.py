def chromosome_check(sperm):
    sperm = 'X' + str(sperm)
    print(sperm)
    if sperm == 'XY':
        print('Congratulations! You\'re going to have a son.')
        return 'Congratulations! You\'re going to have a son.'
    elif sperm == 'XX':
        print('Congratulations! You\'re going to have a daughter.')
        return 'Congratulations! You\'re going to have a daughter.'
    else:
        print("Invalid Input")


# def chromosome_check(sperm):
#     return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')


def chromosome_check(sperm):
    gender = {"XY": "son", "XX": "daughter"}

    return "Congratulations! You're going to have a {}.".format(gender[sperm])


chromosome_check('Y')
chromosome_check('X')
