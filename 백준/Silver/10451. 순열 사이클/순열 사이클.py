import sys


list_ = []

T = int(sys.stdin.readline())

def dfs(v):
    n = len(v)
    visited = set()
    count = 0  # 사이클 개수 초기화

    for start in range(1, n + 1):
        if start not in visited:
            stack = [start]
            visited.add(start)
            while stack:
                node = stack.pop()
                next_node = v[node - 1]
                if next_node not in visited:
                    stack.append(next_node)
                    visited.add(next_node)
            count += 1
    return count


for _ in range(T):
    N = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split()))
    list_.append(dfs(values))


for a in list_:
    print(a)
