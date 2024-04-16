def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer == []:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            answer.pop()
            i += 1
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1
    if answer == []:
        return [-1]
    return answer