def solution(s1, s2):
    answer = 0
    for a in s2:
        if a in s1:
            answer += 1
    return answer