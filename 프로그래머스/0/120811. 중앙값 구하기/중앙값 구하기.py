def solution(array):
    answer = 0
    list_ = sorted(array)
    answer = list_[len(list_) // 2]
    return answer