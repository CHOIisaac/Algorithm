def solution(food):
    answer = ''
    for a in range(1, len(food)):
        if (food[a] / 2) >= 1:
            print(a)
            answer += str(a)*(food[a] // 2)
    return answer+'0'+answer[::-1]