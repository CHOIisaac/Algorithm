def solution(n, computers):
    def dfs(node):

        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    visited = [False] * n  
    network_count = 0    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
    return network_count