def solution(n):
    answer = [n]
    for i in range(n):
        if n == 1:
            continue
        if n % 2 == 0:
            answer.append(n/2)
            n = n/2
        elif n % 2 == 1:
            answer.append(3*n+1)
            n = 3*n+1
    return answer