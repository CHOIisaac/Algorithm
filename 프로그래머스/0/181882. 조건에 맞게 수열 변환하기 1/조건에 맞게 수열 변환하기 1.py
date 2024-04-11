def solution(arr):
    answer = []
    # answer = [arr[i] % 2 for i in arr if arr[i] > 50 elif arr[i] * 2]
    for a in arr:
        if a >= 50 and a % 2 == 0:
            answer.append(a/2)
        elif a < 50 and a % 2 ==1:
            answer.append(a*2)
        else:
            answer.append(a)
    return answer