def solution(my_string):
    answer = 0
    for a in my_string:
        if a.isdigit():
            answer += int(a)
    return answer