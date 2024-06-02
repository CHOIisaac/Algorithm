def solution(n):
    answer = 0
    ternary = ''
    while n:
        n, remainder = divmod(n, 3)
        ternary = str(remainder) + ternary
        
    length = len(ternary)
    
    for i in range(length):
        answer += int(ternary[::-1][i]) * (3 ** (length - 1 - i))
    return answer