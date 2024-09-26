def solution(num_list):
    answer = [0, 0]
    for  a in num_list:
        if a % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer