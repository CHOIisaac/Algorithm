def solution(num, k):
    answer = 0
    index = str(num).find(str(k))
    if index == -1:
        answer = -1
    else:
        answer = index + 1
    return answer