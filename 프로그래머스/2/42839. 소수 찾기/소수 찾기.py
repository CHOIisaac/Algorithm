from itertools import permutations


def is_perm(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    set_ = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            set_.add(int(''.join(perm)))
    
    answer = sum(1 for a in set_ if is_perm(a))
    
    return answer