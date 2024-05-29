def solution(left, right):
    answer = 0
    aa = []
    for i in range(left, right+1):
        aa = []
        for j in range(1, i+1):
            if i % j == 0:
                aa.append(j)
        if len(aa) % 2 == 1:
            answer -= i
        elif len(aa) % 2 == 0:
            answer += i
    return answer