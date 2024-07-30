from itertools import combinations
import math

def solution(nums):
    answer = 0
    list_ = []
    for c in combinations(nums, 3):
        list_.append(sum(c))
    
    for a in list_:
        flag = True
        for b in range(2, int(math.sqrt(a)+1)):
            if a % b == 0:
                flag = False
                break
        if flag:
            answer += 1
    # for i in range(2, int(math.sqrt(sum(combi))+1)):
    #     print(1)
    return answer