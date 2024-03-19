def solution(a, b, c):
    answer = a+b+c if a != b != c != a else (a+b+c)*(a*a+b*b+c*c)*(a**3+b**3+c**3) if a == b == c else (a+b+c)*(a*a+b*b+c*c)
    
    return answer