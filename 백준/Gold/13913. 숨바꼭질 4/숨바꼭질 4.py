import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def bfs(start):
    q = deque()
    q.append(start)
    graph[start] = 0

    while q:
        node = q.popleft()

        next_node = [node+1, node-1, node*2]
        
        for i in next_node:
            if 0 <= i < 100001:
                if graph[i] == INF:
                    graph[i] = graph[node] + 1
                    dp[i] = node # 직전 노드 저장
                    q.append(i)

graph = [INF] * 100001

N, K = map(int,input().split())

dp = [-1] * 100001

bfs(N)

print(graph[K])

path = []
current = K

while current != -1:
    path.append(current)
    current = dp[current]
path.reverse() 

print(*path)
