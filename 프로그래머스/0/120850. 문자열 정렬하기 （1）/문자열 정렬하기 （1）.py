def solution(my_string):
    answer = []
    for a in my_string:
        if a.isdigit():
            answer.append(int(a))
    answer.sort()
    return answer