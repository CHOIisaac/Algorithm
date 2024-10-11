def solution(s):
    answer = 0
    result = s. split()
    for i in range(len(result)):
        if result[i] == "Z":
            answer -= int(result[i-1])
        else:
            answer += int(result[i])
    return answer