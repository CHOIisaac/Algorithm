def solution(k, score):
    answer = []
    a = []
    for i in score:
        a.append(i)
        a.sort(reverse=True)
        
        if len(a) > k:
            a.pop()
            
        answer.append(a[-1])
    return answer