def correct(string):
    return string.translate(str.maketrans("501", "SOI"))


def replace_dots(str):
    print((str.replace(".", "-")))
    return str.replace(".", "-")


replace_dots("one.two.three")