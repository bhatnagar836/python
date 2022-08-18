import math


def dating_range(age):
    if age > 14:
        minimum = math.floor((age/2)+7)
        maximum = math.floor((age - 7)*2)
    else:
        minimum = math.floor(age - 0.10 * age)
        maximum = math.floor(age + 0.10 * age)
    print(f"{minimum}-{maximum}")
    return f"{minimum}-{maximum}"


dating_range(26)