def solution(sides):
    answer = 0
    max_side = max(sides)
    min_side = min(sides)
    
    answer = (max_side + min_side - 1) - (max_side - min_side)
    return answer