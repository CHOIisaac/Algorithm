def solution(my_string, m, c):
    answer = ''
    result = []
    for i in range(0, len(my_string), m):
        result += [my_string[i:m+i]]
    for j in result:

        answer += j[c-1]
    return answer