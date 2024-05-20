def solution(n):
    answer = 0
    a = list(str(n))
    a.sort(reverse=True)
    c = ''.join(a)
    answer = int(c)
    return answer