def solution(my_strings, parts):
    answer = ''
    for i, a in enumerate(parts):
        answer += my_strings[i][a[0]:a[1]+1]

    return answer