def solution(a, b):
    first = str(a) + str(b)
    second = str(b) + str(a)
    if int(first) > int(second):
        answer = first
    else:
        answer =second
    
    return int(answer)