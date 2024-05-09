def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        char = ''
        for j in range(len(picture[i])):
            char += picture[i][j]*k
        for a in range(k):
            answer.append(char)
    return answer