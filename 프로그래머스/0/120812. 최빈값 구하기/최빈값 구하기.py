def solution(array):
    answer = []
    aa = {}
    for a in array:
        if a in aa:
            aa[a] += 1
        else:
            aa[a] = 1
    max_ = max(aa.values())
    for key, value in aa.items():
        if value == max_:
            answer.append(key)        
    return answer[0] if len(answer) == 1 else -1