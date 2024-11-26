def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    if set(lost) & set(reserve):
        list_ = set(lost) & set(reserve)
        for a in list_:
            lost.remove(a)
            reserve.remove(a)
    for i in lost:
        for j in reserve:
            if abs(i - j) == 1:
                answer += 1
                reserve.remove(j)
                break
    answer += n - len(lost)   
    return answer