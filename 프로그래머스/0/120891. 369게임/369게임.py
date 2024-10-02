def solution(order):
    answer = 0
    for a in str(order):
        if int(a) == 3 or int(a) == 6 or int(a) == 9:
            answer += 1
    return answer