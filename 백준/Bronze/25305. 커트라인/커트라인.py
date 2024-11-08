import sys

N, K = map(int, sys.stdin.readline().split())

list_ = list(map(int, sys.stdin.readline().split()))

list_.sort(reverse=True)

print(list_[K-1])
