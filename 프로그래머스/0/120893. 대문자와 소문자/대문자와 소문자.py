def solution(my_string):
    answer = ''
    for a in my_string:
        if a.isupper():
            answer += a.lower()
        elif a.islower():
            answer += a.upper()
    return answer