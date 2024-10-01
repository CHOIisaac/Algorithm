def solution(sides):
    answer = 1
    max_ = max(sides)
    sides.remove(max_)
    if max_ >= sum(sides):
        answer = 2
        
    return answer