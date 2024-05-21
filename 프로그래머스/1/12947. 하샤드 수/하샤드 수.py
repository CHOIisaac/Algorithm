def solution(x):
    answer = True
    digits = list(str(x))
    digits = list(map(int, digits))
    if x % sum(digits) != 0:
        answer = False
    return answer