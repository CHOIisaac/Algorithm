def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i == ' ':
            cnt = 0
            answer += i
            continue
        if cnt % 2 == 0:
            answer += i.upper()
        elif cnt % 2 == 1:
            answer += i.lower()
        
        cnt += 1
    print(answer)
    return answer