def enough(cap, on, wait):
    return 0 if cap >= on + wait else  on + wait - cap
    # if cap >= on + wait:
    #     print(0)
    #     return 0
    # else:
    #     print(on + wait - cap)
    #     return on + wait - cap

enough(100, 60, 50)