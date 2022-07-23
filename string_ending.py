def solution(string, ending):
    print(True) if string[len(string)-len(ending):] == ending else print(False)
    return True if string[len(string)-len(ending):] == ending else False


solution('abcdeafas', 'afas')
solution('abcde', 'cde')
