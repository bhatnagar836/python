# kata8
import re


def validate_hello(greetings):
    bool_val = False
    greet_list = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    x = re.split(",| |_|-|!|\?|;|:|\.", greetings.lower())
    # print(x)

    for items in x:
        if items in greet_list:
            bool_val = True
        else:
            pass

    if bool_val:
        print(True)
        return True
    else:
        print(False)
        return False


# def validate_hello(greetings):
#     return any(x in greetings.lower() for x in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])



validate_hello('hAstA! TREs: ARE La dOIng cZesc. HAstA! Que? BIen:')
validate_hello('hombre! Hola!')
