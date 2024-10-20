def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]
        next_term = common[-1] + d
        answer = next_term
    
    elif common[1] // common[0] == common[2] // common[1]:
        r = common[1] // common[0] 
        next_term = common[-1] * r
        answer = next_term
    return answer