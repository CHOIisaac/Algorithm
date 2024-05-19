def solution(s):
    answer = True
    string = s.lower()
    if string.count('p') != string.count('y'):
        answer = False

    return answer