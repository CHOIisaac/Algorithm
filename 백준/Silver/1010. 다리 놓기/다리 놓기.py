import sys

arr = []

T = int(sys.stdin.readline())


def cal(m, n):
    result = 1
    for i in range(m-n):
        result *= (m-i)
        result //= (i+1)
    return result


for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr.append(cal(M, N))

for a in arr:
    print(a)
