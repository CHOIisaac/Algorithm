def solution(n):
    answer = 0
    def gcd(a, b):
        while b != 0:
            a, b = b, a%b
        return a
    answer = abs(6 * n) // gcd(6, n)
    return answer // 6