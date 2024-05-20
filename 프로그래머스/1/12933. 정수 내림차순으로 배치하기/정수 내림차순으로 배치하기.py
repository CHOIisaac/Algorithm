def solution(n):
    answer = 0
    a = list(map(int, str(n)))
    b = sorted(a, reverse=True)
    c = ''.join(map(str, b))
    answer = int(c)
    return answer