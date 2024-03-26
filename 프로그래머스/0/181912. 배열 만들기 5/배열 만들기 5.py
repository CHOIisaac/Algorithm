def solution(intStrs, k, s, l):
    answer = []
    for a in intStrs:
        result = a[s:l+s]
        if int(result) > k:
            answer.append(int(result))
    return answer