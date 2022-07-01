def solution(a, b):
    print(b+a+b) if len(a) > len(b) else print(a+b+a)
    return b+a+b if len(a) > len(b) else a+b+a


solution('Soon', 'Me')