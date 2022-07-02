def well(x):
    # print(f'"good" appears {x.count("good")} time(s)')
    # print(f'"bad" appears {x.count("bad")} time(s)')
    if x.count("good") == 1 or x.count("good") == 2:
        print('Publish!')
        return 'Publish!'
    elif x.count("good") >= 2:
        print('I smell a series!')
        return 'I smell a series!'
    else:
        print('Fail!')
        return 'Fail!'


# def well(x):
#     c = x.count('good')
#     return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'

well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'])
well(['good', 'bad', 'bad', 'bad', 'bad'])
well(['bad', 'bad', 'bad'])