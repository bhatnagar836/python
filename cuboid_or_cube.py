def cube_checker(volume, side):
    if volume <= 0:
        return False
    else:
        vol2 = side*side*side
        if vol2 == volume:
            return True
        else:
            return False


cube_checker(27, 3)
# True
cube_checker(1, 5)
# False
cube_checker(125, 5)
# True
cube_checker(125,-5)
# False