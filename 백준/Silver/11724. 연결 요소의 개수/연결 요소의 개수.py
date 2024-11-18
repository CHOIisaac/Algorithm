import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

list_ = []

for _ in range(N + 1):
    list_.append([])

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    list_[a].append(b)
    list_[b].append(a)

visited = [False for _ in range(N+1)]
count = 0


def dfs(v):
    visited[v] = True
    for i in list_[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)


for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)
