def solution(number):
    answer = 0
    num = sum(list(map(int, list(number))))
    print(sum(list(map(int, list(number)))))
    print()
    answer = sum(list(map(int, list(number)))) % 9
    return answer