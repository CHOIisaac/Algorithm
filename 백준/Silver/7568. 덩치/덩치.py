import sys

list_ = []
N = int(sys.stdin.readline())

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    list_.append((weight, height))

rank_list = [1] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        elif list_[i][0] < list_[j][0] and list_[i][1] < list_[j][1]:
            rank_list[i] += 1

print(" ".join(map(str, rank_list)))