import math

def solution(n):
    answer = -1
    num = math.sqrt(n)

    if num == int(num):
        answer = (num+1)**2
    return answer