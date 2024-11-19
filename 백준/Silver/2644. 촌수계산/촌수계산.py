import sys


sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

list_ = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = list(map(int, sys.stdin.readline().split()))
    list_[x].append(y)
    list_[y].append(x)

visited = [False for _ in range(N+1)]


def dfs(v, count):
    visited[v] = True
    count += 1
    if v == b:
        return count - 1
    for i in list_[v]:
        if not visited[i]:
            val = dfs(i, count)
            if val != -1:
                return val
    return -1


result = dfs(a, 0)
print(result)

