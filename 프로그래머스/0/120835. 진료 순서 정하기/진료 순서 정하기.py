def solution(emergency):
    answer = []
    list_ = sorted(emergency, reverse=True)
    for a in emergency:
        answer.append(list_.index(a)+1)
    return answer