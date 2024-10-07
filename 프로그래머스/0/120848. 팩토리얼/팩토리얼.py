def solution(n):
    factorial = 1  # 초기값 1 (0! = 1)
    i = 1          # 팩토리얼 계산을 위한 시작 값

    # n 이하의 가장 큰 팩토리얼을 찾기 위한 반복문
    while factorial <= n:
        i += 1
        factorial *= i  # i!를 계산

    return i - 1  # i!가 n을 넘었을 때, 그 이전의 i - 1이 답