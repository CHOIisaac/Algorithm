import sys

from collections import deque


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

list_ = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    list_[a].append(b)
    list_[b].append(a)


def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    count = 0

    while queue:
        node, depth = queue.popleft()
        if depth > 2:
            continue
        if depth > 0:
            count += 1

        for v in list_[node]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, depth+1))
    return count


print(bfs(1))