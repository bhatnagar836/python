def fake_bin(x):
    new_word = ''
    for item in x:
        if int(item) < 5:
            new_word = new_word + '0'
        elif int(item) >= 5:
            new_word = new_word + '1'
    print(new_word)
    return new_word


fake_bin('45385593107843568')