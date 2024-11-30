def solution(n, computers):
    def dfs(node):
        # 현재 노드 방문 처리
        visited[node] = True
        
        # 연결된 모든 노드 탐색
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    visited = [False] * n  # 방문 여부 배열
    network_count = 0      # 네트워크 개수
    
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터에서 DFS 시작
            dfs(i)
            network_count += 1  # 새로운 네트워크 발견
    
    return network_count