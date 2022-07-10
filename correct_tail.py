def correct_tail(body, tail):
    length = len(body)
    sub = body[length-1]
    if sub == tail:
        return True
    else:
        return False


# def correct_tail(body, tail):
#     return body.endswith(tail)


correct_tail("Fox", "x")