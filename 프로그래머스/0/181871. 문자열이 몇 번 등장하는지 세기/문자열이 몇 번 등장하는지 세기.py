def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if pat in myString[i:len(pat)+i]:
            answer += 1
    return answer