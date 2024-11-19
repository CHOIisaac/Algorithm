import sys


while True:
    list_ = []
    N = int(sys.stdin.readline())
    if N == 0:
        break

    for _ in range(N):
        list_.append(sys.stdin.readline().strip())
    print(sorted(list_, key=lambda x: x.lower())[0])