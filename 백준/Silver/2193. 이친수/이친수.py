import sys


N = int(sys.stdin.readline())


a, b = 1, 1
for _ in range(3, N + 1):
    a, b = b, a + b


print(b)