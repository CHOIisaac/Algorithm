def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = 1
        for a in num_list:
            answer *= a
    return answer