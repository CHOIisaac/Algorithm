def solution(num_list):
    answer = 0
    mul = 1
    dou = sum(num_list)**2
    for num in num_list:
        mul *= num
    print(mul)
    print(dou)
    return 1 if dou > mul else 0