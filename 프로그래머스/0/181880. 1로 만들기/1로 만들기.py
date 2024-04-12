def solution(num_list):
    answer = 0
    for a in num_list:
        count = 0
        while a != 1:
            count += 1
            if a % 2 == 0:
                a = a / 2
            elif a % 2 ==1:
                a = (a-1) / 2
        answer += count
    return answer