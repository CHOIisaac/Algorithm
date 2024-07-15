from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(enumerate(priorities))
    while queue:
        data = queue.popleft()
        if any(data[1] < queue[i][1] for i in range(len(queue))):
            queue.append(data)
        else:
            answer += 1
            if data[0] == location:
                break
    return answer