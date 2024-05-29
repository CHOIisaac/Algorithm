def solution(num):
    answer = 0
    aa = num
    while aa != 1:
        answer += 1
        if aa % 2 == 0:
            aa = aa // 2
        elif aa % 2 == 1:
            aa = aa * 3 + 1
    if answer > 500:
        return -1
    return answer