def solution(strArr):
    tmp = []
    getarr = [0] * len(strArr)
    for i in strArr:
        getarr[len(i)] += 1
    return max(getarr)