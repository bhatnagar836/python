def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        print("Too much clothes")
        return "Too much clothes"
    elif clothes < load:
        print("Not enough clothes")
        return "Not enough clothes"
    elif clothes > load:
        result = "{:.2f}".format(water * 1.1 ** (clothes - load))
        print(float(result))
        return float(result)
    else:
        return water


how_much_water(50,15,29)
how_much_water(10,10,2)
how_much_water(10,10,21)
how_much_water(10,11,20)