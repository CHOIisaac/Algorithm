def solution(brown, yellow):
    answer = []
    n = brown+yellow
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            w = n // i
            if (w - 2) * ( i - 2) == yellow:
                answer = [w, i]
    return answer