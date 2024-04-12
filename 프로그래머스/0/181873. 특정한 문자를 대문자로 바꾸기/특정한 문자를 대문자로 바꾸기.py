def solution(my_string, alp):
    answer = my_string
    for i in range(len(my_string)):
        if my_string[i] == alp:
            answer = my_string.replace(my_string[i], alp.upper())
            
    return answer