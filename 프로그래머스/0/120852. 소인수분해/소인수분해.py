def solution(n):
    answer = []
    i = 2
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            answer.append(i)
    if n >= 1:
        answer.append(n)
    return sorted(set(answer))