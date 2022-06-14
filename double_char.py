def double_char(s):
    new_word = ""
    for x in s:
        word = x + x
        new_word = new_word + word

    print(new_word)
    return new_word




double_char("String")