def solution(my_string, s, e):
    answer = ''
    print(my_string[s:e])
    print(my_string[s:e][::-1])
    answer = my_string.replace(my_string[s:e+1], my_string[s:e+1][::-1])
    return answer