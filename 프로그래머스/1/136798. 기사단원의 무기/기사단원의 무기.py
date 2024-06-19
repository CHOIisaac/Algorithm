import math

def solution(number, limit, power):
    list_ = []
    for i in range(1, number +1):
        count = 0
        for j in range(1, int(i**0.5) +1):
            if i % j == 0:
                # list_.append(j)
                count += 1
                if ( (j**2) != i):
                    # list_.append(i//j)
                    count += 1
        print(count)
        if count > limit:
            list_.append(power)
        else:
            list_.append(count)
    return sum(list_)