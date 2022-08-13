import math
def find_next_power(val, pow_):
    actual_num = math.ceil(val**(1/pow_))
    return actual_num**pow_
