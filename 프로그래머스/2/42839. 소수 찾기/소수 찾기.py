from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    all_combinations = set()
    
    # 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            number = int(''.join(perm))
            all_combinations.add(number)
    
    # 소수 개수 카운트
    prime_count = sum(1 for num in all_combinations if is_prime(num))
    
    return prime_count