def solution(array, n):
    answer = min(array, key=lambda x: (abs(x - n), x))
    return answer