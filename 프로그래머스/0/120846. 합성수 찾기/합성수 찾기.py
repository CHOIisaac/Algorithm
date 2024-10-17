def solution(n):
    answer = 0
    for i in range(4, n+1):
        sum = 0
        for j in range(1, i+1):
            if i % j == 0:
                sum += 1
        if sum >= 3:
            answer += 1
    return answer