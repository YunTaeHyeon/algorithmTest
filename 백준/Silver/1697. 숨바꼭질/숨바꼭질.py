from collections import deque
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        current, dist = q.popleft()

        if current == K:
            return dist
        
        next_positions = [current + 1, current - 1, current * 2]

        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, dist + 1))

    return -1 

visited = [False] * 100001

N, K = map(int, input().split())

result = bfs(N)
print(result)
