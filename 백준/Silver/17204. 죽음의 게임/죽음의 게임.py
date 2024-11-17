import sys


N, M = map(int, sys.stdin.readline().split())

list_ = [int(sys.stdin.readline()) for _ in range(N)]

visited = 0
count = 0

for _ in range(N):
    choice = list_[visited]
    count += 1

    if choice == M:
        print(count)
        break
    visited = choice
else:
    print(-1)

