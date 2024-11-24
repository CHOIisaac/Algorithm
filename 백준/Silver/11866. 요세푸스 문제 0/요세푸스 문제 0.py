import sys

from collections import deque


N, K = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, N + 1)])

list_ = []

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    list_.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, list_)), end='>')
