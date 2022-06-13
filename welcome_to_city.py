def say_hello(name, city, state):
    word = ''
    for i in name:
        word = word + i + " "

    # print(word)

    print("Hello, " + word.strip() + "! Welcome to " + city + ", " + state + "!")
    return "Hello, " + word.strip() + "! Welcome to " + city + ", " + state + "!"

#
# def say_hello(name, city, state):
#   return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)


# Hello, John Smith! Welcome to Phoenix, Arizona!
say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')