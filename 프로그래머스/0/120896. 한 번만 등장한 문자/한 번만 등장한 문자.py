def solution(s):
    answer = []
    for a in s:
        if s.count(a) == 1:
            answer.append(a)
    answer.sort()      
    return ''.join(answer)