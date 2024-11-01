def solution(s):
    answer = True
    a = []
    for x in s:
        if x == '(':
            a.append(x)
        elif x == ')':
            if a:
                a.pop()
            else:
                answer = False
    else:
        if a:
            answer = False
    return answer