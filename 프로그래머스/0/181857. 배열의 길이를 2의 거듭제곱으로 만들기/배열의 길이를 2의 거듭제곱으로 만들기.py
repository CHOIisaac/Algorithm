def solution(arr):
    a = 0
    answer = []
    c = len(arr)
    while c > 1:
        c = c / 2
        a += 1
    return arr + [0]*(2**a - len(arr))