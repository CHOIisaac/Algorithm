def solution(n, control):
    answer = n
    for a in control:
        if a == 'w':
            answer += 1
        elif a == 's':
            answer -= 1
        elif a == 'd':
            answer += 10
        elif a == 'a':
            answer -= 10
    return answer