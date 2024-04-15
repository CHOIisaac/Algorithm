def solution(strArr):
    answer = []
    for a in strArr:
        if not "ad" in a:
            answer.append(a)
    return answer