def solution(strArr):
    answer = []
    for i, a in enumerate(strArr):
        if i % 2 == 1:
            answer.append(a.upper())
        else:
            answer.append(a.lower())
    return answer