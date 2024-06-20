from collections import deque

def solution(maps):
    answer = -1
    N, M = len(maps), len(maps[0])
    
    dy = 1, -1, 0, 0
    dx = 0, 0, 1, -1
    
    list_ = []
    
    queue = deque()
    queue.append((0,0,1))
    
    visited = set()
    visited.add((0,0))
    
    while queue:
        y, x, cnt = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if maps[ny][nx] != 1:
                continue
            if (ny, nx) in visited:
                continue
            
            queue.append((ny, nx, cnt+1))
            visited.add((ny, nx))
        if y == N -1 and x ==M -1:
            answer = cnt
    return answer