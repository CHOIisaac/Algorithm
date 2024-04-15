def solution(myString, pat):
    answer = ''
    print(myString.find('dE'))
    if myString.endswith(pat):
        return myString
    else:
        return myString[:myString.rfind(pat)+len(pat)]
    return answer