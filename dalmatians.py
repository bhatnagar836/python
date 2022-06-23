# if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
# return respond
# Correcting the above program
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        respond = dogs[0]
    elif n <= 50:
        respond = dogs[1]
    elif n <= 100:
        respond = dogs[2]
    else:
        respond = dogs[3]
    return respond

